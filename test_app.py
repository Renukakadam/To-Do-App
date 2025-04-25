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

def test_get_tasks_initially_empty(client):
    response = client.get('/api/tasks')
    assert response.status_code == 200
    assert response.get_json() == []

def test_add_task(client):
    response = client.post('/api/tasks', json={'task': 'Buy groceries'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['task'] == 'Buy groceries'
    assert 'id' in data

def test_add_task_without_content(client):
    response = client.post('/api/tasks', json={})
    assert response.status_code == 400
    assert response.get_json()['error'] == 'Task required'

def test_delete_task(client):
    # Add a task first
    add_response = client.post('/api/tasks', json={'task': 'To be deleted'})
    task_id = add_response.get_json()['id']

    # Now delete the task
    delete_response = client.delete(f'/api/tasks/{task_id}')
    assert delete_response.status_code == 200
    assert delete_response.get_json()['message'] == 'Task deleted'
