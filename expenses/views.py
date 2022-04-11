from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from expenses.models import Expense
from . import forms

AMOUNT_RANGES = {
    "cheap": "Cheap (<$10)",
    "regular": "Regular ($10-$100)",
    "expensive": "Expensive (>$100)",
}

AMOUNT_RANGES_Q = {
    "cheap": Q(amount__lt=10),
    "regular": Q(amount__gte=10, amount__lte=100),
    "expensive": Q(amount__gt=100),
}


@login_required
def expense_list(request: HttpRequest):
    qs = Expense.objects
    if q := request.GET.get("q", "").strip():
        qs = qs.filter(title__icontains=q)
    if amount_range := request.GET.get("amount_range", ""):
        arq = AMOUNT_RANGES_Q.get(amount_range)
        if arq:
            qs = qs.filter(arq)
    total = sum(
        o.amount for o in qs.all()
    )  # TODO: use SQL based aggregation==sum(amount)
    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs,
            "total": total,
            "q": q,
            "amount_range": amount_range,
            "AMOUNT_RANGES": AMOUNT_RANGES,
        },  # <--- CONTEXT
    )


@login_required
def expense_detail(request: HttpRequest, pk: int):
    o = get_object_or_404(Expense, id=pk)

    return render(
        request,
        "expenses/expense_detail.html",
        {
            "object": o,
        },
    )


@login_required
def expense_create(request: HttpRequest):
    if request.method == "POST":
        form = forms.ExpenseForm(request.POST)
        if form.is_valid():
            o = form.save()
            return redirect(o)
            # return redirect(reverse("expenses:list"))
        # fallthrough!!!!
    else:
        form = forms.ExpenseForm()
    return render(
        request,
        "expenses/expense_form.html",
        {
            "form": form,
        },
    )


@login_required
def expense_update(request: HttpRequest, pk: int):
    o = get_object_or_404(Expense, id=pk)
    if request.method == "POST":
        form = forms.ExpenseForm(request.POST, instance=o)
        if form.is_valid():
            o = form.save()
            messages.info(request, f"Update expense #{o.id} successfully.")
            return redirect(o)
        # fallthrough!!!!
    else:
        form = forms.ExpenseForm(instance=o)
    return render(
        request,
        "expenses/expense_form.html",
        {
            "object": o,
            "form": form,
        },
    )


@login_required
def expense_delete(request: HttpRequest, pk: int):
    o = get_object_or_404(Expense, id=pk)
    if request.method == "POST":
        oid = o.id
        o.delete()
        messages.success(request, f"Deleted expense #{oid} successfully.")
        return redirect(reverse("expenses:list"))

    return render(
        request,
        "expenses/expense_confirm_delete.html",
        {
            "object": o,
        },
    )
