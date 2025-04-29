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

def test_representative_edit(representative):

    token = login_jwt(representative)

    headers = {
        "Authorization": f"Bearer {token}"
    }

    representative_id = 6

    body_request = {
        "email": "dududueedu@email.com"
    }

    route_response = representative.put(f"/representative/{representative_id}", headers=headers, json=body_request)

   

    assert route_response.status_code == 200
    assert route_response.json["email"]

   

    
