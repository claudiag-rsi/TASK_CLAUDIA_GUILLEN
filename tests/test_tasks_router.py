import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.models import Task, UpdateTaskModel, TaskList
from app.db import db

client = TestClient(app)

def test_create_task():
    task_data = {"id": 1, "title": "Test Task", "description": "This is a test task", "completed": False}
    response = client.post("/tasks/", json=task_data)
    assert response.status_code == 200
    assert response.json() == task_data

def test_get_task():
    task_id = 1
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id

def test_get_task_not_found():
    task_id = 999
    response = client.get(f"/tasks/{task_id}")
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_get_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
    assert isinstance(response.json()["tasks"], list)

def test_update_task():
    task_id = 1
    update_data = {"title": "Updated Task", "description": "This task has been updated", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 200
    assert response.json()["title"] == update_data["title"]
    assert response.json()["description"] == update_data["description"]
    assert response.json()["completed"] == update_data["completed"]

def test_update_task_not_found():
    task_id = 999
    update_data = {"title": "Updated Task", "description": "This task has been updated", "completed": True}
    response = client.put(f"/tasks/{task_id}", json=update_data)
    assert response.status_code == 404
    assert response.json()["detail"] == "Task not found"

def test_delete_all_tasks():
    response = client.delete("/tasks/all")
    assert response.status_code == 200
    assert response.json()["mensaje"] == "Todas las tareas han sido eliminadas"

def test_delete_task():
    task_id = 1
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Task deleted successfully"

