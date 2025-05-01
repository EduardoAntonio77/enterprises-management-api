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

def test_enterprise_delete(client, login_jwt):
    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"
    }

    client_id = 4

    route_response = client.delete(f"/client/{client_id}", headers=headers)
    print(f"Resposta da API: {route_response.json}")

    assert route_response.status_code == 200