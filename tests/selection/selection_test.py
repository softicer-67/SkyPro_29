import pytest


@pytest.mark.django_db
def test_create_selection(client, ad, user, admin_token):
    data = {
        "name": "New User",
        "items": [ad.id],
        "owner": user.id
    }

    expected_response = {
        "id": 1,
        "name": "New User",
        "items": [ad.id],
        "owner": user.id
    }

    response = client.post("/selection/", data,
                           content_type="application/json",
                           HTTP_AUTHORIZATION=f'Bearer {admin_token}'
                           )

    assert response.status_code == 201
    assert response.data == expected_response
