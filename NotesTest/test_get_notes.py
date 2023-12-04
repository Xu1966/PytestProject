import pytest
import requests


def test_get_all_notes_with_valid_creds(valid_login):
    headers = {'x-auth-token': f'{valid_login}'}
    response = requests.get(f"{pytest.BASE_URL}/notes", headers=headers, verify=False)
    assert response.status_code == 200
    assert response.json()["message"] == "Notes successfully retrieved"


def test_get_all_notes_with_no_header(valid_login):
    response = requests.get(f"{pytest.BASE_URL}/notes", verify=False)
    assert response.status_code == 401
    assert response.json()["message"] == "No authentication token specified in x-auth-token header"

@pytest.mark.parametrize("id",["656dbc4103e2430141921b5c"])
def test_get_note_with_valid_id(valid_login,id):
    headers = {'x-auth-token': f'{valid_login}'}
    response = requests.get(f"{pytest.BASE_URL}/notes/{id}", headers=headers, verify=False)
    assert response.status_code == 200
    assert response.json()["message"] == "Note successfully retrieved"

def test_get_specific_note_with_no_header():
    response = requests.get(f"{pytest.BASE_URL}/notes/642a08826a35ca02115ea350", verify=False)
    assert response.status_code == 401
    assert response.json()["message"] == "No authentication token specified in x-auth-token header"


@pytest.mark.parametrize("id", ["656dbc4103e2430141921b5qowi"])
def test_get_note_with_no_id_from_database(valid_login, id):
    headers = {'x-auth-token': f'{valid_login}'}
    response = requests.get(f'{pytest.BASE_URL}/notes/api/notes/{id}',headers=headers, verify=False)
    assert response.status_code == 404
    assert response.json()["message"] == "Not Found"


def test_get_note_with_invalid_id_type(valid_login):
    headers = {'x-auth-token': f'{valid_login}'}
    response = requests.get(f'{pytest.BASE_URL}/notes/abcd',headers=headers, verify=False)
    assert response.status_code == 400
    assert response.json()["message"] == "Note ID must be a valid ID"
