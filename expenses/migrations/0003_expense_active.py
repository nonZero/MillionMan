# Generated by Django 4.0.3 on 2022-05-16 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("expenses", "0002_alter_comment_expense"),
    ]

    operations = [
        migrations.AddField(
            model_name="expense",
            name="active",
            field=models.BooleanField(default=True),
        ),
    ]