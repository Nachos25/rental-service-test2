from django.core.management.base import BaseCommand
from django.db import transaction

from apps.apartments.factories import UserFactory, ApartmentFactory


class Command(BaseCommand):
    help = 'Generates test data for apartments and users'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            default=5,
            type=int,
            help='Number of users to create'
        )
        parser.add_argument(
            '--apartments',
            default=20,
            type=int,
            help='Number of apartments to create'
        )

    @transaction.atomic
    def handle(self, *args, **options):
        user_count = options['users']
        apartment_count = options['apartments']

        self.stdout.write(f'Creating {user_count} users...')
        users = [UserFactory() for _ in range(user_count)]

        self.stdout.write(f'Creating {apartment_count} apartments...')
        apartments = []

        # Create apartments with existing users
        for i in range(apartment_count):
            user_index = i % user_count  # Distribute apartments among users
            apartment = ApartmentFactory(owner=users[user_index])
            apartments.append(apartment)

        success_msg = (
            f'Successfully created {user_count} users '
            f'and {apartment_count} apartments.'
        )
        self.stdout.write(self.style.SUCCESS(success_msg))
