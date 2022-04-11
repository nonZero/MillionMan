import random

import silly
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction, IntegrityError
from faker import Faker

from expenses.models import Expense, Category, Comment


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
            with transaction.atomic():
                Comment.objects.all().delete()
                Expense.objects.all().delete()

        faker = Faker()

        users = []
        for i in range(1, 10):
            un = f"user{i}"
            try:
                users.append(
                    User.objects.create_user(
                        username=un,
                        password="secret",
                        email=f"{un}@example.com",
                    )
                )
            except IntegrityError:
                users.append(User.objects.get(username=un))

        while Category.objects.count() < 10:
            Category.objects.create(
                name=faker.word(),
                priority=random.randint(10, 200),
            )
        cats = list(Category.objects.all())
        for i in range(n):
            o = Expense.objects.create(
                user=random.choice(users),
                category=random.choice(cats),
                title=f"{silly.adjective()} {silly.noun()}",
                amount=random.randint(100, 30000) / 100,
                date=faker.date_this_year(),
                description=faker.paragraph(),
            )
            for i in range(int(random.normalvariate(2, 1))):
                o.comments.create(
                    created_by=random.choice(users)
                    if random.randint(1, 5) == 1
                    else o.user,
                    content="\n".join(faker.sentences(3)),
                    is_todo=random.randint(1, 10) == 7,
                )
