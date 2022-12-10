import factory

from ads.models import Ad, Category
from ads.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = 'maxi'
    password = '123qwe'


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "new_test"
    price = 100
    description = "testing description"
    is_published = False


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('name')
    slug = factory.Faker('color')
