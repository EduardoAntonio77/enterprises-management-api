import pytest
from app import App
from tests.conftests import representative

def login_jwt(representative):
    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = representative.post("/login", json=login_request)
    return response.json["access_token"]


def test_representative_get(representative):
    
    token = login_jwt(representative)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    route_response = representative.get("/representative", headers=headers)

    assert route_response.status_code == 200
    assert isinstance(route_response.json, list)

    for repre in route_response.json:
        assert "name" in repre
        assert "id" in repre
        