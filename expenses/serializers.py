from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = (
            "id",
            "name",
        )


class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = models.Expense
        fields = (
            "id",
            "category",
            "user",
            # "category",
            "title",
            "amount",
            "date",
            "description",
        )
