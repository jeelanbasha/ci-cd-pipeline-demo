import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b"WRONG TEXT" in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data

def test_api_test(client):
    response = client.get('/api/test')
    assert response.status_code == 200
    assert b"success" in response.data