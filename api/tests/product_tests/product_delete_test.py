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

def test_enterprise_delete(product, login_jwt):
    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"
    }

    product_id = 3

    route_response = product.delete(f"/product/{product_id}", headers=headers)

    assert route_response.status_code == 200