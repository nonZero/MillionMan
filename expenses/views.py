import random

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from expenses.models import Expense, Comment
from . import forms
from .forms import CommentForm
from .serializers import ExpenseSerializer


class ExpenseViewSet(ModelViewSet):
    queryset = Expense.objects.filter(active=True)
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)


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


class AllExpensesBaseView(LoginRequiredMixin):
    model = Expense

    def get_queryset(self):
        return (
            super().get_queryset()
            # TODO: Refactor: move to Manager qs.active().for_user(user)
            .filter(
                user=self.request.user,
            )
        )


class ExpenseBaseView(AllExpensesBaseView):
    def get_queryset(self):
        return (
            super().get_queryset()
            # TODO: Refactor: move to Manager qs.active().for_user(user)
            .filter(
                active=True,
            )
        )


class ExpenseJsonView(ExpenseBaseView, ListView):
    def get(self, request, *args, **kwargs):
        qs = self.get_queryset()
        return JsonResponse(
            {
                "status": "ok",
                "expenses": [
                    {
                        "id": o.id,
                        "title": o.title,
                        "amount": o.amount,
                        "date": o.date,
                        "category": o.category,
                    }
                    for o in qs
                ],
            }
        )


class ExpenseListView(ExpenseBaseView, ListView):
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        if q := self.request.GET.get("q", "").strip():
            qs = qs.filter(title__icontains=q)
        return qs

    def get_context_data(self, **kwargs):
        d = super().get_context_data(
            **kwargs,
        )
        d["total"] = sum(
            o.amount for o in d["object_list"]
        )  # TODO: use SQL based aggregation==sum(amount)
        d["grand_total"] = sum(
            o.amount for o in self.get_queryset()
        )  # TODO: use SQL based aggregation==sum(amount)
        return d


class ExpenseDetailView(AllExpensesBaseView, DetailView):
    model = Expense

    def get_context_data(self, **kwargs):
        d = super().get_context_data(**kwargs)
        d["form"] = CommentForm()
        return d


class ExpenseCreateView(ExpenseBaseView, SuccessMessageMixin, CreateView):
    model = Expense
    form_class = forms.ExpenseForm
    success_message = "Expense created."

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class ExpenseUpdateView(ExpenseBaseView, UpdateView):
    form_class = forms.ExpenseForm


class ExpenseDeleteView(ExpenseBaseView, DeleteView):
    success_url = reverse_lazy("expenses:list")

    def form_valid(self, form):
        self.object.safe_delete()
        return redirect(self.get_success_url())


class CommentCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Comment
    fields = (
        "content",
        "is_todo",
    )
    success_message = "Comment created."

    def get_success_url(self):
        return self.get_expense().get_absolute_url()

    def get_expense(self):
        return get_object_or_404(
            Expense,
            id=self.kwargs["pk"],
            user=self.request.user,
        )

    def get_context_data(self, **kwargs):
        d = super().get_context_data(**kwargs)
        d["expense"] = self.get_expense()
        return d

    def form_valid(self, form):
        form.instance.expense = self.get_expense()
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class RandomView(View):
    def get(self, request, **kwargs):
        return HttpResponse(f"SHALOM {random.randint(1, 100)}!")
