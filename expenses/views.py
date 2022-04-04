from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import render

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
    if q := request.GET.get("q", "").strip():
        qs = qs.filter(title__icontains=q)
    if amount_range := request.GET.get("amount_range", ""):
        arq = AMOUNT_RANGES_Q.get(amount_range)
        if arq:
            qs = qs.filter(arq)
    total = sum(o.amount for o in qs)  # TODO: use SQL based aggregation==sum(amount)
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
