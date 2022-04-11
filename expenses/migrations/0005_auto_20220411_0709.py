from django.db import migrations


def assign_to_general_category(apps, schema_editor):
    Category = apps.get_model("expenses", "Category")
    Expense = apps.get_model("expenses", "Expense")
    c, created = Category.objects.get_or_create(name="General")
    Expense.objects.filter(category=None).update(category=c)


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0004_category_alter_expense_description_and_more"),
    ]

    operations = [
        migrations.RunPython(assign_to_general_category),
    ]
