from calendar import HTMLCalendar

from django.http import HttpRequest
from django.shortcuts import render

from expenses.models import Expense


def expense_list(request: HttpRequest):
    # assert False, request.GET["q"]
    qs = Expense.objects.all()
    # if "q" in request.GET:
    #     qs = qs.filter(title__icontains=request.GET["q"])
    # q = request.GET.get("q", "").strip()
    # if q:
    #     qs = qs.filter(title__icontains=q)

    if q := request.GET.get("q", "").strip():
        qs = qs.filter(title__icontains=q)
    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs,
        },  # <--- CONTEXT
    )
