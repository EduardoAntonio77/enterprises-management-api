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

    enterprise_id = 2

    route_response = client.delete(f"/client/{enterprise_id}", headers=headers)

    assert route_response.status_code == 200