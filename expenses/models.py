from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone


class Expense(models.Model):
    # created_at = models.DateTimeField(auto_now_add=True)
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
