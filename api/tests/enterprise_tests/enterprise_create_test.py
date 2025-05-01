import pytest
from tests.conftests import enterprise

@pytest.fixture
def login_jwt(enterprise):

    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = enterprise.post("/login", json=login_request)
    return response.json["access_token"]

def test_enterprise_success(enterprise, login_jwt):
    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"
    }

    body_request = {
        "name": "kakakaka",
        "client_quantity": 1000,
        "address": "Rua que fica em algum lugar ai",
        "phone": "55 11 12233123123",
        "representative_id": 9 
    }

    route_response = enterprise.post("/enterprise", json=body_request, headers=headers)


    print("Resposta da rota:", route_response.json)
    assert route_response.status_code == 200 
    assert route_response.json["message"] == 'Successfully registered enterprise'


def test_enterprise_missing_field(enterprise, login_jwt):

    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"  
    }

    body_request = {
        "name": "Joao AutoPecas",
        "client_quantity": 1000,
        "address": "Rua que fica em algum lugar ai",
        "phone": "55 11 9999-9999"
    }

    route_response = enterprise.post("/enterprise", json=body_request, headers=headers)

    assert route_response.status_code == 400
