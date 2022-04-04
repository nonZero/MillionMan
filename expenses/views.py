from calendar import HTMLCalendar

from django.http import HttpRequest
from django.shortcuts import render

from expenses.models import Expense


def expense_list(request: HttpRequest):
    qs = Expense.objects.all()
    # print(request.GET.getlist("my_search_fields"))
    if q := request.GET.get("q", "").strip():
        qs = qs.filter(title__icontains=q)
    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs,
        },  # <--- CONTEXT
    )
