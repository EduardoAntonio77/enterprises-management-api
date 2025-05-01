import pytest
from tests.conftests import enterprise  # ou como estiver nomeado seu client de teste

@pytest.fixture
def login_jwt(enterprise):
    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = enterprise.post("/login", json=login_request)
    return response.json["access_token"]

def test_enterprise_edit(enterprise, login_jwt):
    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"
    }

    enterprise_id = 2  

    body_request = {
        "name": "Nova Empresadasd LTDA",
        "email": "novaasdempresa@email.com",
        "address": "Rua Novaasd, 456"
    }

    route_response = enterprise.put(f"/enterprise/{enterprise_id}", headers=headers, json=body_request)
    

    print(f"Resposta da API:{route_response.json}")
    assert route_response.status_code == 200
    assert route_response.json["message"] == "Enterprise updated successfully"
