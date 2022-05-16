import random

import silly
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import transaction, IntegrityError
from faker import Faker

from blog.models import Post


class Command(BaseCommand):
    help = "Creates fake posts"

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
                Post.objects.all().delete()

        faker = Faker()

        for i in range(n):
            o = Post.objects.create(
                title=f"{silly.adjective()} {silly.noun()}",
                posted_at=faker.date_this_year(),
                teaser=faker.paragraph(),
                content="\n".join(
                    faker.paragraph() for i in range(random.randint(3, 8))
                ),
            )
