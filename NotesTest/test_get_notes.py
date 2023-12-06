import pytest
import requests

"""
    -Retrieve all notes with Valid authorization.

    Returns:
    Retrieve all notes with status code 200

"""


@pytest.mark.smoke
@pytest.mark.regression
def test_get_all_notes_with_valid_creds(valid_login):
    response = requests.get(f"{pytest.BASE_URL}/notes", headers=valid_login, verify=False)
    assert response.status_code == 200
    assert response.json()["message"] == "Notes successfully retrieved"


"""
    -Retrieve all notes with Invalid authorization.

    Returns:
    Throws validation error with status code 401

"""


@pytest.mark.sanity
@pytest.mark.regression
def test_get_all_notes_with_no_header(valid_login):
    response = requests.get(f"{pytest.BASE_URL}/notes", verify=False)
    assert response.status_code == 401
    assert response.json()["message"] == "No authentication token specified in x-auth-token header"


"""
    -Retrieve specific notes with Valid authorization and valid ID.

    Returns:
    Retrieve specific note with status code 200

"""


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("id", ["656dbc4103e2430141921b5c"])
def test_get_note_with_valid_id(valid_login, id):
    response = requests.get(f"{pytest.BASE_URL}/notes/{id}", headers=valid_login, verify=False)
    assert response.status_code == 200
    assert response.json()["message"] == "Note successfully retrieved"


"""
    -Retrieve specific note with Invalid authorization.

    Returns:
    Throws validation error with status code 401

"""


@pytest.mark.sanity
@pytest.mark.regression
def test_get_specific_note_with_no_header():
    response = requests.get(f"{pytest.BASE_URL}/notes/642a08826a35ca02115ea350", verify=False)
    assert response.status_code == 401
    assert response.json()["message"] == "No authentication token specified in x-auth-token header"


"""
    -Retrieve specific note with Valid authorization and ID which is not present in database.

    Returns:
    Throws not found error with status code 404

"""


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.parametrize("id", ["656dbc4103e2430141921b5qowi"])
def test_get_note_with_no_id_from_database(valid_login, id):
    response = requests.get(f'{pytest.BASE_URL}/notes/api/notes/{id}', headers=valid_login, verify=False)
    assert response.status_code == 404
    assert response.json()["message"] == "Not Found"


"""
    -Retrieve specific note with Valid authorization and invalid ID .

    Returns:
    Throws bad request with status code 400

"""


@pytest.mark.sanity
@pytest.mark.regression
def test_get_note_with_invalid_id_type(valid_login):
    response = requests.get(f'{pytest.BASE_URL}/notes/abcd', headers=valid_login, verify=False)
    assert response.status_code == 400
    assert response.json()["message"] == "Note ID must be a valid ID"
