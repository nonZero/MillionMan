from django.shortcuts import render


def expense_list(request):
    products = [
        "coffee",
        "ice cream",
        "cookies",
        "bananas",
        "melon",
    ]
    return render(
        request,
        "expenses/expense_list.html",
        {
            "kuku123": 456789,
            "foo19": "shalom    <b>hi</b>",
            "products": products,
        },
    )
