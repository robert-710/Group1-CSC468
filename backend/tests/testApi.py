import pytest
from app import app as flask_app

@pytest.fixture
def app():
    yield flask_app

@pytest.fixture
def client(app):
    return app.test_client()

def test_get_scenic_locations(client):
    response = client.get('/api/scenic-locations')
    assert response.status_code == 200
    # Add more assertions based on your data

def test_insert_scenic_location(app, client):
    response = client.post('/api/scenic-locations', json={
        'name': 'Sunset Point',
        'description': 'A beautiful spot to watch the sunset',
        'latitude': 40.7128,
        'longitude': -74.0060
    })
    assert response.status_code == 201
    assert response.json['name'] == 'Sunset Point'
