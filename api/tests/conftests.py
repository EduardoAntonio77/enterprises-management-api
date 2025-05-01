import pytest
from app import App

@pytest.fixture
def representative():
    app_instance = App()
    app = app_instance.app
    app.config['TESTING'] = True

    with app.test_client() as representative:
        yield representative

@pytest.fixture
def enterprise():
    app_instance = App()
    app = app_instance.app
    app.config['TESTING'] = True

    with app.test_client() as enterprise:
        yield enterprise

@pytest.fixture
def client():
    app_instance = App()
    app = app_instance.app
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client

@pytest.fixture
def product():
    app_instance = App()
    app = app_instance.app
    app.config['TESTING'] = True

    with app.test_client() as product:
        yield product


