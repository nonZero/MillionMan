import random

from django.core.management.base import BaseCommand
from faker import Faker

from expenses.models import Expense, Category

faker = Faker()


class Command(BaseCommand):
    help = "Creates fake expenses"

    def add_arguments(self, parser):
        parser.add_argument(
            "n",
            type=int,
            help="Number of fake expenses to create",
        )
        parser.add_argument(
            "--delete",
            action="store_true",
            help="delete all expenses",
        )

    def handle(self, n: int, delete: bool, *args, **options):
        if delete:
            Expense.objects.all().delete()
        while Category.objects.count() < 10:
            Category.objects.create(
                name=faker.word(),
                priority=random.randint(10, 200),
            )
        cats = list(Category.objects.all())
        for i in range(n):
            Expense.objects.create(
                category=random.choice(cats),
                title=faker.sentence(),
                amount=random.randint(100, 30000) / 100,
                date=faker.date_this_year(),
                description=faker.paragraph(),
            )
