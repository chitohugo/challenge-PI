def test_sign_up(client):
    payload = {
        "email": "jonathan.robert.williams@aol.com",
        "username": "somberstem",
        "first_name": "Jonathan",
        "last_name": "Williams",
        "password": "sapien"
    }
    response = client.post(
        "/api/v1/auth/sign-up",
        json=payload
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["email"] == "jonathan.robert.williams@aol.com"
    assert response_json["username"] == "somberstem"


def test_sign_in(create_user, client):
    payload = {
        "email": "julian.clark@gmail.com",
        "password": "dolor"
    }
    response = client.post(
        "/api/v1/auth/sign-in",
        json=payload
    )
    assert response.status_code == 200
    response_json = response.json()
    assert response_json["access_token"] is not None
