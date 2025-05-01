import pytest
from tests.conftests import product

def login_jwt(product):
    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = product.post("/login", json=login_request)
    return response.json["access_token"]

def test_client_get_filter(product):

    token = login_jwt(product)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    product_id = 3

    route_response = product.get(f"product/{product_id}", headers=headers)

    
    assert route_response.status_code == 200