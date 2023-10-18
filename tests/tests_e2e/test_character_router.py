def test_create_character(client, token):
    payload = {
        "id": 2,
        "name": "Cleaning Item",
        "height": 18.2,
        "mass": 10.2,
        "hair_color": "Uranian blue",
        "skin_color": "Blue",
        "eye_color": "White"
    }

    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = client.post(
        "/api/v1/character/",
        headers=headers,
        json=payload,
    )

    assert response.status_code == 200
    response_json = response.json()
    assert response_json["name"] == "Cleaning Item"
    assert response_json["eye_color"] == "White"


def test_get_all_characters(client, token):
    headers = {
        "Authorization": f"Bearer {token}"
    }
    response = client.get(
        "/api/v1/character/",
        headers=headers
    )
    assert response.status_code == 200
    response = response.json()
    assert len(response["items"]) == 1
