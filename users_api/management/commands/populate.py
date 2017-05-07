from django.core.management.base import BaseCommand, CommandError
from faker import Factory

from users_api.models import User

fake = Factory.create('sv_SE')


class Command(BaseCommand):
    help = 'Create a bunch of fake users'

    def handle(self, *args, **options):
        for id in range(25):
            u = User(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.safe_email(),
                birthday=fake.date(pattern="%Y-%m-%d")
            )
            u.save()
