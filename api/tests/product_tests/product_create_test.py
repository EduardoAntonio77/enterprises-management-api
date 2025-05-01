import pytest
from tests.conftests import product

@pytest.fixture
def login_jwt(product):

    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = product.post("/login", json=login_request)
    return response.json["access_token"]

def test_product_success(product, login_jwt):
    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"
    }

    body_request = {
        "name": "Copo",
        "price": 10,
        "stock": 1000,
        "enterprise_id": 2
    }

    route_response = product.post("/product", json=body_request, headers=headers)

    print("Resposta da rota:", route_response.json)
    assert route_response.status_code == 200 
    assert route_response.json["message"] == 'Successfully registered product'

def test_enterprise_missing_field(product,  login_jwt):

    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"  
    }

    body_request = {
        "name": "Copo",
        "price": 10,
        "enterprise_id": 2
    }

    route_response = product.post("/enterprise", json=body_request, headers=headers)

    assert route_response.status_code == 400

