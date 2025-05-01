import pytest
from tests.conftests import client

def login_jwt(client):
    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = client.post("/login", json=login_request)
    return response.json["access_token"]

def test_client_get_filter(client):

    token = login_jwt(client)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    client_id = 1

    route_response = client.get(f"client/{client_id}", headers=headers)

    response = route_response.json

    print(f"resposta da api: {response}")
    assert route_response.status_code == 200


