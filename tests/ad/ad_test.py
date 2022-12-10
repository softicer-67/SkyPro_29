import pytest

from tests.factories import AdFactory
from ads.serializers import AdSerializer


@pytest.mark.django_db
def test_ad_list(client, admin_token):
    ad = AdFactory.create_batch(5)
    expected_response = {
        'count': 5,
        'next': None,
        'previous': None,
        'results': AdSerializer(ad, many=True).data
    }

    response = client.get('/ad/', format='json', HTTP_AUTHORIZATION='Bearer ' + admin_token)

    assert response.status_code == 200
    assert response.data == expected_response
