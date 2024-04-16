from fastapi.testclient import TestClient
from main import app #Import your FastAPI app instance


client = TestClient(app)


def test_create_user_success():
    user_data = {
        "username":"testuser",
        "email":"test@example.com",
        "password": "StrongPassword123"
    }
    response = client.post("/users/",json=user_data)
    assert response.status_code == 200
    assert response.json() == user_data

def test_create_user_invalid_password():
    user_data = {
        "username": "testuser",
        "email":"test@example.com",
        "password": "weak"

    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 400
    assert "Password must be at least 8 characters long" in response.text

def test_create_user_missing_lowercase():
    user_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "UPPERCASEONLY"
    }
    response = client.post("/users/", json=user_data)
    assert response.status_code == 400
    assert "Password must contain both uppercase and lowercase characters" in response.text
