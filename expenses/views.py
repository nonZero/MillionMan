from functools import reduce
import operator

from django.db.models import Q
from django.http import HttpRequest, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from . import forms

from expenses.models import Expense

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


def expense_list(request: HttpRequest):
    qs = Expense.objects
    if amount_range := request.GET.get("amount_range", ""):
        arq = AMOUNT_RANGES_Q.get(amount_range)
        if arq:
            qs = qs.filter(arq)

    search_fields = []
    if q := request.GET.get("q", "").strip():
        if not (search_fields := request.GET.getlist("my_search_fields")):
            # if fields to search were not specified via checkboxes, search them all
            search_fields = [f.name for f in Expense._meta.get_fields()]  # QUESTION: use fields or get_fields()?
        search_clauses = [(f'{fld}__icontains', q) for fld in search_fields]
        q_list = [Q(clause) for clause in search_clauses]
        qs = qs.filter(reduce(operator.or_, q_list))

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
            "search_fields": search_fields,
            "amount_range": amount_range,
            "AMOUNT_RANGES": AMOUNT_RANGES,
        },  # <--- CONTEXT
    )


def expense_detail(request: HttpRequest, pk: int):
    o = get_object_or_404(Expense, id=pk)

    return render(
        request,
        "expenses/expense_detail.html",
        {
            "object": o,
        },
    )


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
