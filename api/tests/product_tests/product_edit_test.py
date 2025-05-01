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

def test_product_edit(product, login_jwt):
    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"
    }

    product_id = 4

    body_request = {
        "name": "Caneca"
    }

    route_response = product.put(f"product/{product_id}", headers=headers, json=body_request)

    print(f"Resposta da API:{route_response.json}")
    assert route_response.status_code == 200
    assert route_response.json["message"] == "Product updated successfully"