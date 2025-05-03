import factory
from factory.django import DjangoModelFactory
from factory import fuzzy
from decimal import Decimal

from django.contrib.auth import get_user_model
from .models import Apartment

User = get_user_model()


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: f'user{n}')
    email = factory.LazyAttribute(lambda obj: f'{obj.username}@example.com')
    password = factory.PostGenerationMethodCall('set_password', 'password')
    is_active = True


class ApartmentFactory(DjangoModelFactory):
    class Meta:
        model = Apartment

    name = factory.Faker('sentence', nb_words=3)
    description = factory.Faker('paragraph')
    price = fuzzy.FuzzyDecimal(Decimal('500.00'), Decimal('5000.00'))
    number_of_rooms = fuzzy.FuzzyInteger(1, 5)
    square = fuzzy.FuzzyDecimal(Decimal('30.00'), Decimal('150.00'))
    availability = fuzzy.FuzzyChoice([True, False])
    owner = factory.SubFactory(UserFactory) 