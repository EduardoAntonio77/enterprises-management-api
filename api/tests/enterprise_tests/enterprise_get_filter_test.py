import pytest
from tests.conftests import enterprise

def login_jwt(enterprise):
    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = enterprise.post("/login", json=login_request)
    return response.json["access_token"]

def test_enterprise_get_filter(enterprise):
    token = login_jwt(enterprise)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    enterprise_id = 7

    route_response = enterprise.get(f"/enterprise/{enterprise_id}", headers=headers)

    response = route_response.json

    print(f"resposta da api: {response}")
    assert route_response.status_code == 200
    assert "id" in response
    assert "name" in response
    assert "address" in response
