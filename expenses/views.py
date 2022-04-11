from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpRequest, HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

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

# CBV: CLASS BASED VIEWS


class ExpenseBaseView(LoginRequiredMixin):
    model = Expense

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


class ExpenseListView(ExpenseBaseView, ListView):
    paginate_by = 10

    # ordering = "-title"
    # paginate_by = 15

    # def get(self, request: HttpRequest):
    #     qs = Expense.objects.filter(user=request.user)
    #     if q := request.GET.get("q", "").strip():
    #         qs = qs.filter(title__icontains=q)
    #     if amount_range := request.GET.get("amount_range", ""):
    #         arq = AMOUNT_RANGES_Q.get(amount_range)
    #         if arq:
    #             qs = qs.filter(arq)
    #     total = sum(
    #         o.amount for o in qs.all()
    #     )  # TODO: use SQL based aggregation==sum(amount)
    #     return render(
    #         request,
    #         "expenses/expense_list.html",
    #         {
    #             "object_list": qs,
    #             "total": total,
    #             "q": q,
    #             "amount_range": amount_range,
    #             "AMOUNT_RANGES": AMOUNT_RANGES,
    #         },  # <--- CONTEXT
    #     )


class ExpenseDetailView(ExpenseBaseView, DetailView):
    model = Expense


# @login_required
# def expense_detail(request: HttpRequest, pk: int):
#     o = get_object_or_404(Expense, id=pk, user=request.user)
#
#     return render(
#         request,
#         "expenses/expense_detail.html",
#         {
#             "object": o,
#         },
#     )


class ExpenseCreateView(ExpenseBaseView, SuccessMessageMixin, CreateView):
    model = Expense
    form_class = forms.ExpenseForm
    success_message = "Expense created."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


# @login_required
# def expense_create(request: HttpRequest):
#     if request.method == "POST":
#         form = forms.ExpenseForm(request.POST)
#         if form.is_valid():
#             o: Expense = form.instance
#             o.user = request.user
#             form.save()
#             return redirect(o)
#             # return redirect(reverse("expenses:list"))
#         # fallthrough!!!!
#     else:
#         form = forms.ExpenseForm()
#     return render(
#         request,
#         "expenses/expense_form.html",
#         {
#             "form": form,
#         },
#     )


class ExpenseUpdateView(ExpenseBaseView, UpdateView):
    form_class = forms.ExpenseForm


class ExpenseDeleteView(ExpenseBaseView, DeleteView):
    success_url = reverse_lazy("expenses:list")


#
# @login_required
# def expense_update(request: HttpRequest, pk: int):
#     o = get_object_or_404(Expense, id=pk, user=request.user)
#     if request.method == "POST":
#         form = forms.ExpenseForm(request.POST, instance=o)
#         if form.is_valid():
#             o = form.save()
#             messages.info(request, f"Update expense #{o.id} successfully.")
#             return redirect(o)
#         # fallthrough!!!!
#     else:
#         form = forms.ExpenseForm(instance=o)
#     return render(
#         request,
#         "expenses/expense_form.html",
#         {
#             "object": o,
#             "form": form,
#         },
#     )
#
#
# @login_required
# def expense_delete(request: HttpRequest, pk: int):
#     o = get_object_or_404(Expense, id=pk, user=request.user)
#     if request.method == "POST":
#         oid = o.id
#         o.delete()
#         messages.success(request, f"Deleted expense #{oid} successfully.")
#         return redirect(reverse("expenses:list"))
#
#     return render(
#         request,
#         "expenses/expense_confirm_delete.html",
#         {
#             "object": o,
#         },
#     )
#
#
# class View:
#     def dispatch(self, request, **kwargs):
#         func = getattr(self, request.method, None)
#         if func is None:
#             return HttpResponseNotAllowed(f"Could not {request.method} to this view.")
#         return func(request, **kwargs)
#
#     @classmethod
#     def as_view(cls):
#         o = cls()
#
#         def view(request, **kwargs):
#             o.request = request
#             o.kwargs = kwargs
#             return o.dispatch(request, **kwargs)
#
#         return view
#
#
# class MyView(View):
#     def get(self, request, **kwargs):
#         return render(...)
#
#
#
# the_view = MyView.as_view()
