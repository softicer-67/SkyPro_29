import pytest


@pytest.mark.django_db
def test_create_ad_1(client, admin_token):
    data_to_send = {
        "author": None,
        "category": None,
        "name": "Proba_new_test",
        "price": str(0),
        "description": "new description",
        "is_published": False,
        "image": None
    }
    expected_response = {
        "id": 7,
        "author": None,
        "category": None,
        "name": "Proba_new_test",
        "price": str(0),
        "description": "new description",
        "is_published": False,
        "image": None
    }
    print("Ensure this field has at least 0 characters.")

    response = client.post("/ad/", data_to_send,
                           content_type='application/json',
                           HTTP_AUTHORIZATION=f'Bearer {admin_token}')

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad_2(client, admin_token):
    data_to_send = {
        "name": "Proba_new_test",
        "price": str(200),
        "description": "Proba description",
        "image": None,
        "is_published": False,
        "author": None,
        "category": None
    }
    expected_response = {
        "id": 8,
        "name": "Proba_new_test",
        "price": str(200),
        "description": "Proba description",
        "image": None,
        "is_published": False,
        "author": None,
        "category": None
    }

    response = client.post("/ad/", data_to_send,
                           content_type='application/json',
                           HTTP_AUTHORIZATION=f'Bearer {admin_token}')

    assert response.status_code == 201
    assert response.data == expected_response
