import pytest
from tests.conftests import enterprise  # ou o client do Flask
# certifique-se de que login_jwt esteja disponível

@pytest.fixture
def login_jwt(enterprise):
    # Login para obter JWT válido
    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = enterprise.post("/login", json=login_request)
    return response.json["access_token"]


def test_product_get_success(enterprise, login_jwt):
    # Teste de sucesso para obter produtos

    token = login_jwt
    headers = {
        "Authorization": f"Bearer {token}"
    }

    response = enterprise.get("/enterprise", headers=headers)

    assert response.status_code == 200
    assert isinstance(response.json, list)