import pytest
import requests
from utils.util import get_notes


@pytest.mark.parametrize("id,title,description,category", get_notes())
def test_create_note_successfully(valid_login, id, title, description, category):
    headers = {'x-auth-token': f'{valid_login}'}
    data = {
        "id": id,
        "title": title,
        "description": description,
        "category": category
    }
    response = requests.post(f"{pytest.BASE_URL}/notes", headers=headers, data=data, verify=False)
    assert response.status_code == 200
    assert response.json().get("message") == "Note successfully created"


@pytest.mark.parametrize("id,title,description,category", [("3", "test4", "this is new test", "Work")])
def test_create_note_without_login(id, title, description, category):
    data = {
        "id": id,
        "title": title,
        "description": description,
        "category": category
    }
    response = requests.post(f"{pytest.BASE_URL}/notes", data=data, verify=False)
    assert response.status_code == 401
    assert response.json().get("message") == "No authentication token specified in x-auth-token header"


def test_create_note_with_invalid_payload(valid_login):
    headers = {'x-auth-token': f'{valid_login}'}
    data = {
        "title": "Invalid payload"
    }
    response = requests.post(f"{pytest.BASE_URL}/notes", headers=headers, data=data, verify=False)
    assert response.status_code == 400


def test_create_note_with_invalid_title(valid_login):
    headers = {'x-auth-token': f'{valid_login}'}
    data = {
        "id": 10,
        "title": "Tes",
        "description": "This is for invalid title",
        "category": "Home"
    }
    response = requests.post(f"{pytest.BASE_URL}/notes", data=data, headers=headers, verify=False)
    print("Hello world")
    print(response.status_code)
    assert response.status_code == 400
    assert response.json().get("message") == "Title must be between 4 and 100 characters"


def test_create_note_with_invalid_category(valid_login):
    headers = {'x-auth-token': f'{valid_login}'}
    data = {
        "id": 10,
        "title": "Test",
        "description": "This is for invalid title",
        "category": "None"
    }
    response = requests.post(f"{pytest.BASE_URL}", data=data, headers=headers, verify=False)
    assert response.status_code == 404

