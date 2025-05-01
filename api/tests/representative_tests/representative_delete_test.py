import pytest
from tests.conftests import representative

@pytest.fixture
def login_jwt(representative):
    login_request = {
        "email": "fanta@email.com",
        "password": "101010"
    }

    response = representative.post("/login", json=login_request)
    return response.json["access_token"]

def test_representative_delete(representative, login_jwt):

    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"
    }

    representative_id = 6

    route_response = representative.delete(f"/representative/{representative_id}", headers=headers)

    assert route_response.status_code == 200
