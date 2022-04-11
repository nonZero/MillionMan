from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):
    name = models.CharField(max_length=300, blank=False, unique=True)
    priority = models.IntegerField(default=100)

    def __str__(self):
        return self.name


class Expense(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.PROTECT, related_name="expenses"
    )
    category = models.ForeignKey(Category, models.PROTECT, related_name="expenses")
    title = models.CharField(
        max_length=300,
        validators=[
            MinLengthValidator(2),
        ],
    )
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    date = models.DateField(default=timezone.now)
    description = models.TextField(default="", blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("expenses:detail", kwargs={"pk": self.id})

    def is_expensive(self):
        return self.amount > 75


class Comment(models.Model):
    expense = models.ForeignKey(Expense, models.PROTECT, related_name="comments")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.PROTECT, related_name="comments"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    is_todo = models.BooleanField(default=False)
