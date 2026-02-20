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
    assert b"Hello World" in response.data

def test_health(client):
    response = client.get('/health')
    assert response.status_code == 200
    assert b"healthy" in response.data

def test_api_test(client):
    response = client.get('/api/test')
    assert response.status_code == 200
    assert b"success" in response.data

def test_health_returns_json(client):
    response = client.get('/health')
    data = response.get_json()
    assert data['status'] == 'healthy'

def test_api_test_returns_correct_value(client):
    response = client.get('/api/test')
    data = response.get_json()
    assert data['result'] == 'success'
    assert data['value'] == 42

def test_404_on_invalid_route(client):
    response = client.get('/nonexistent')
    assert response.status_code == 404