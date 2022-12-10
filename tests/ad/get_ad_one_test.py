import pytest

from ads.serializers import AdSerializer


@pytest.mark.django_db
def test_retrieve_ad(client, ad, admin_token):
    expected_response = {
        'id': ad.id,
        'category': None,
        'author': None,
        'name': 'new_test',
        'price': str(100),
        'description': "testing description",
        'is_published': False,
        'image': None
    }

    response = client.get(f'/ad/{ad.id}/', HTTP_AUTHORIZATION=f'Bearer {admin_token}')

    assert response.status_code == 200
    assert response.data == expected_response
