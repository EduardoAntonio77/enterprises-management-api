import pytest
from tests.conftests import representative

def login_jwt(representative):
    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = representative.post("/login", json=login_request)
    return response.json["access_token"]

def test_representative_get_filter(representative):

    token = login_jwt(representative)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    representative_id = 9

    route_response = representative.get(f"/representative/{representative_id}", headers=headers)

    assert route_response.status_code == 200
    response = route_response.json
    assert "id" in response
    assert "name" in response
    assert "cnpj" in response
    assert "email" in response
    assert "phone" in response
    assert "created_at" in response