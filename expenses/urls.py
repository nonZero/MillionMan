from django.urls import path

from . import views

app_name = "expenses"

urlpatterns = [
    path("", views.ExpenseListView.as_view(), name="list"),
    path("<int:pk>/", views.ExpenseDetailView.as_view(), name="detail"),
    path("<int:pk>/edit/", views.ExpenseUpdateView.as_view(), name="update"),
    path("<int:pk>/delete/", views.ExpenseDeleteView.as_view(), name="delete"),
    path("create/", views.ExpenseCreateView.as_view(), name="create"),
]
