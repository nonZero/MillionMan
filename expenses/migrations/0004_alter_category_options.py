# Generated by Django 4.0.3 on 2022-05-16 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0003_expense_active"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name_plural": "categories"},
        ),
    ]
