from django.db import models

# ORM: Object-Relational Mapper

# SQL: DDL + DML
        # Data Definition Language
        # Data Manipulation Language


class Expense(models.Model):
    title = models.CharField(max_length=300)
    amount = models.DecimalField(decimal_places=2, max_digits=11)
    date = models.DateField()

    def __str__(self):
        return self.title
