import pytest


@pytest.fixture()
def my_fixture():
    return 1


@pytest.fixture
@pytest.mark.django_db
def admin_token(client, django_user_model):
    username = 'admin'
    password = '123'

    django_user_model.objects.create_user(
        username=username, password=password, role='admin')

    response = client.post(
        '/token/',
        {'username': username, 'password': password},
        format='json'
    )

    return response.data['access']
