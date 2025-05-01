import pytest
from tests.conftests import client

@pytest.fixture

def login_jwt(client):

    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = client.post("/login", json=login_request)
    return response.json["access_token"]

def test_client_success(client, login_jwt):

    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"
    }

    body_request = {
        "name": "Joaquimm",
        "region": "Osascoo",
        "phone": "112382323123123",
        "cpf": "2837293223",
        "enterprise_id": 2
    }

    route_response = client.post("/client", json=body_request, headers=headers)

    print("Resposta da rota:", route_response.json)
    assert route_response.status_code == 200
    assert route_response.json["message"] == 'Successfully registered client'