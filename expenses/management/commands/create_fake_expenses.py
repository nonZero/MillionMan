import random

from django.core.management.base import BaseCommand
from faker import Faker

from expenses.models import Expense

faker = Faker()


class Command(BaseCommand):
    help = "Creates fake expenses"

    def add_arguments(self, parser):
        parser.add_argument("n", type=int)

    def handle(self, n, *args, **options):
        for i in range(n):
            Expense.objects.create(
                title=faker.sentence(),
                amount=random.randint(100, 30000) / 100,
                date=faker.date_this_year(),
                description=faker.paragraph(),
            )
