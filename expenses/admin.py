from django.contrib import admin

from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


class CommentInline(admin.TabularInline):
    model = models.Comment
    extra = 0


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
    inlines = [
        CommentInline,
    ]


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "expense",
        "created_by",
        "created_at",
        "is_todo",
    )
