import pytest
from django.core.exceptions import ValidationError

from . import models


@pytest.mark.django_db
def test_expense_valid():
    o = models.Expense(title="coffee", amount=16)
    o.full_clean()
    o.save()
    assert models.Expense.objects.count() == 1


@pytest.mark.django_db
def test_expense_invalid():
    o = models.Expense(amount=26)
    with pytest.raises(ValidationError) as exc_info:
        o.full_clean()
    ex: ValidationError = exc_info.value
    assert ex.error_dict["title"][0].message == "This field cannot be blank."
