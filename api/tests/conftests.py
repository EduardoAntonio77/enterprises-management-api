import pytest
from app import App

@pytest.fixture
def representative():
    app_instance = App()
    app = app_instance.app
    app.config['TESTING'] = True

    with app.test_client() as representative:
        yield representative

