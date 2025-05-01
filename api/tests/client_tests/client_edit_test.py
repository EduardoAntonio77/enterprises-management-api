import pytest
from app import App  
from tests.conftests import client 

@pytest.fixture
def login_jwt(client):
    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = client.post("/login", json=login_request)  
    return response.json["access_token"]

def test_client_edit(client, login_jwt):
    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"
    }

    client_id = 1  

    body_request = {
        "name": "Cliente Atualizado",
        "email": "atualizado@cliente.com",
        "phone": "+55 11 98765-4321"
    }

    route_response = client.put(f"client/{client_id}", headers=headers, json=body_request)

    assert route_response.status_code == 200
    assert route_response.json["message"] == 'Client updated successfully'
