from calendar import HTMLCalendar

from django.http import HttpRequest
from django.shortcuts import render

from expenses.models import Expense


def expense_list(request: HttpRequest):
    qs = Expense.objects
    # print(request.GET.getlist("my_search_fields"))
    if q := request.GET.get("q", "").strip():
        qs = qs.filter(title__icontains=q)
    if amount_range := request.GET.get("amount_range", ""):
        match amount_range:
            case "cheap":
                qs = qs.filter(amount__lt=10)
            case "regular":
                qs = qs.filter(amount__gte=10, amount__lte=100)
            case "expensive":
                qs = qs.filter(amount__gt=100)
    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs,
            "q": q,
        },  # <--- CONTEXT
    )
