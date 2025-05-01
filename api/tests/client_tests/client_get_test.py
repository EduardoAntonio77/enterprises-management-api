import pytest
from tests.conftests import client

@pytest.fixture
def login_jwt(client):
    # Login para obter JWT válido
    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = client.post("/login", json=login_request)
    return response.json["access_token"]

def test_client_get(client, login_jwt):

    token = login_jwt
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = client.get("/client", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json, list)