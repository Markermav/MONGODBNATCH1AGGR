from django.core.management  import BaseCommand

from faker import Faker
from CRUD.models import People

from random import randrange


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        faker = Faker()

        for _ in range(100):
            People.objects.create(
                name = faker.name(),
                desc = faker.text(50),
                country = faker.country(),
                familymembers = randrange(3,30)
            )

