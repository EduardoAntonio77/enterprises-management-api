import pytest
from tests.conftests import product

def login_jwt(product):
    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = product.post("/login", json=login_request)
    return response.json["access_token"]

def test_representative_get(product):
    
    token = login_jwt(product)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    route_response = product.get("/representative", headers=headers)

    assert route_response.status_code == 200
    assert isinstance(route_response.json, list)


