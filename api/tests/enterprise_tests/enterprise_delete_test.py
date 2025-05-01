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

def test_enterprise_delete(enterprise, login_jwt):
    token = login_jwt

    headers = {
        "Authorization": f"Bearer {token}"
    }

    enterprise_id = 2  

    route_response = enterprise.delete(f"/enterprise/{enterprise_id}", headers=headers)

    assert route_response.status_code == 200
