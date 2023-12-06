import pytest
import requests

"""
    -Update specific note with Valid authorization and valid ID.
    -JSON data is passed as data.

    Returns:
    Updates specific note with status code 200

"""


@pytest.mark.smoke
@pytest.mark.regression
def test_update_note_with_valid_id(valid_login):
    data = {
        "title": "Test23",
        "description": "This is test 3 note",
        "category": "Home",
        "completed": False
    }
    response = requests.put(f"{pytest.BASE_URL}/notes/656ea20003e2430141921dff", headers=valid_login, json=data,
                            verify=False)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Note successfully Updated"


"""
    -Update specific note with Valid authorization and Invalid ID.
    -JSON data is passed as data.

    Returns:
    Throws bad request with status code 400

"""


@pytest.mark.sanity
@pytest.mark.regression
def test_update_note_with_invalid_id(valid_login):
    data = {
        "title": "This is title",
        "description": "This is test 3 note",
        "category": "Home",
        "completed": False
    }
    response = requests.put(f"{pytest.BASE_URL}/notes/-1", headers=valid_login, json=data, verify=False)
    print(response.json())
    assert response.status_code == 400
    assert response.json()["success"] is False
    assert response.json()["message"] == "Note ID must be a valid ID"


"""
    -Update specific note with Invalid authorization.
    -JSON data is passed as data.

    Returns:
    Throws validation error with status code 401

"""


@pytest.mark.sanity
@pytest.mark.regression
def test_update_notes_with_no_header():
    data = {
        "title": "This is title",
        "description": "This is test 3 note",
        "category": "Home",
        "completed": False
    }
    response = requests.put(f"{pytest.BASE_URL}/notes/656ea20003e2430141921dff", json=data, verify=False)
    print(response.json())
    assert response.status_code == 401
    assert response.json()["success"] is False
    assert response.json()["message"] == "No authentication token specified in x-auth-token header"


"""
    -Update specific note with Valid authorization and no payload.

    Returns:
    Throws bad request with status code 400

"""


@pytest.mark.sanity
@pytest.mark.regression
def test_update_notes_with_no_payload(valid_login):
    response = requests.put(f"{pytest.BASE_URL}/notes/656ea20003e2430141921dff", headers=valid_login, verify=False)
    assert response.status_code == 400
    assert response.json()["success"] is False
