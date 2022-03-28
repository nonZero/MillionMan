from calendar import HTMLCalendar

from django.shortcuts import render

from expenses.models import Expense


def expense_list(request):
    products = [
        "coffee",
        "ice cream",
        "cookies",
        "bananas",
        "melon",
    ]
    qs = Expense.objects.all()
    return render(
        request,
        "expenses/expense_list.html",
        {
            "object_list": qs,
            "kuku123": 456789,
            "foo19": "shalom    <b>hi</b>",
            "products": products,
            "nums": [(x, x**2) for x in range(10)],
            "cal": HTMLCalendar().formatmonth(2022, 3),
        },
    )
