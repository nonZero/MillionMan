from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Expense)
class ExpenseAdmin(admin.ModelAdmin):
    date_hierarchy = "date"
    search_fields = (
        "id",
        "title",
        "amount",
        "date",
    )
    list_display = (
        "id",
        "title",
        "amount",
        "date",
    )
