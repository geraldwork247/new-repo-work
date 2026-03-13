import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Test: Activity listing endpoint

def test_list_activities():
    # Arrange
    # ...nothing to arrange for GET request...
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Test: Signup endpoint (valid case)

def test_signup_valid():
    # Arrange
    email = "newstudent@mergington.edu"
    # Act
    response = client.post(f"/activities/Chess Club/signup?email={email}")
    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Signed up {email} for Chess Club"

# Test: Signup endpoint (invalid activity)

def test_signup_invalid_activity():
    # Arrange
    email = "ghost@mergington.edu"
    # Act
    response = client.post(f"/activities/NonExistent/signup?email={email}")
    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"

# Test: Signup endpoint (missing email)

def test_signup_missing_email():
    # Arrange
    # No email provided
    # Act
    response = client.post("/activities/Chess Club/signup")
    # Assert
    assert response.status_code == 422
    # FastAPI returns validation error for missing required fields
