import pytest
import requests
from utils.util import get_notes

"""
    -Create notes with valid authorization and valid payload which are read from file(notes.csv located in config folder).
    
    Returns:
    Notes are created with status code 200.
    
"""


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("id,title,description,category", get_notes())
def test_create_note_successfully(valid_login, id, title, description, category):
    data = {
        "id": id,
        "title": title,
        "description": description,
        "category": category
    }
    response = requests.post(f"{pytest.BASE_URL}/notes", headers=valid_login, json=data, verify=False)
    assert response.status_code == 200
    assert response.json().get("message") == "Note successfully created"


"""
    -Create notes with invalid authorization and payload sent from parameterization used in pytest.

    Returns:
    Throws validation error with status code 401

"""


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.parametrize("id,title,description,category", [("3", "test4", "this is new test", "Work")])
def test_create_note_without_login(id, title, description, category):
    data = {
        "id": id,
        "title": title,
        "description": description,
        "category": category
    }
    response = requests.post(f"{pytest.BASE_URL}/notes", json=data, verify=False)
    assert response.status_code == 401
    assert response.json()["success"] is False
    assert response.json()["message"] == "No authentication token specified in x-auth-token header"


"""
    -Create notes with Valid authorization and invalid payload.

    Returns:
    Throws Bad request with status code 400

"""


@pytest.mark.sanity
@pytest.mark.regression
def test_create_note_with_invalid_payload(valid_login):
    data = {
        "title": "Invalid payload"
    }
    response = requests.post(f"{pytest.BASE_URL}/notes", headers=valid_login, json=data, verify=False)
    assert response.status_code == 400
    assert response.json()["success"] is False


"""
    -Create notes with Valid authorization and invalid title as payload.

    Returns:
    Throws bad request with status code 400

"""


@pytest.mark.sanity
@pytest.mark.regression
def test_create_note_with_invalid_title(valid_login):
    data = {
        "id": 10,
        "title": "Tes",
        "description": "This is for invalid title",
        "category": "Home"
    }
    response = requests.post(f"{pytest.BASE_URL}/notes", json=data, headers=valid_login, verify=False)
    assert response.status_code == 400
    assert response.json().get("message") == "Title must be between 4 and 100 characters"


"""
    -Create notes with Valid authorization and invalid category as payload.

    Returns:
    Throws not found error with status code 400

"""


@pytest.mark.sanity
@pytest.mark.regression
def test_create_note_with_invalid_category(valid_login):
    data = {
        "id": 10,
        "title": "Test",
        "description": "This is for invalid title",
        "category": "None"
    }
    response = requests.post(f"{pytest.BASE_URL}", json=data, headers=valid_login, verify=False)
    assert response.status_code == 404
