import io
import time
import requests
import subprocess
import signal
from fastapi import FastAPI
from fastapi.testclient import TestClient
from tests.main import app, router

client = TestClient(app)

def test_read_name():
    response = client.get("/{name}")
    assert response.status_code == 200
    assert response.json() == {"message" : "Hello World {name}"}

def test_users_get():
    response = client.get("/users/1")
    assert response.status_code == 200
    assert response.json() == {"user":{"name":"John","age":35,"email":"john@fakemail.com","birthday":"2000-01-01"},"query":None}

def test_users_not_found():
    response = client.get("/users/999")
    assert response.status_code == 200
    assert response.json() == {"error": "User not found"} 

def test_upload_file():
    file_content = b"test file"
    file = io.BytesIO(file_content)
    files = {"file": ("testfile.txt", file, "text/plain")}
    response = client.post("/uploadfile/", files=files)
    assert response.status_code == 200
    assert response.json() == {"filename": "testfile.txt"}

def test_users_delete():
    response = client.delete("/users/1")
    assert response.status_code == 200
    assert response.json() == {
    "users": {
        "2": {
            "name": "Jane",
            "age": 25,
            "email": "jane@fakemail.com",
            "birthday": "2010-12-04",
        }
    }
}