import pytest
import requests

"""
    -Delete notes with Valid authorization and valid id.
    -ID sent from parameterization in pytest

    Returns:
    Deletes specific note with status code 200.

"""


@pytest.mark.smoke
@pytest.mark.regression
@pytest.mark.parametrize("id", [("656e0efc03e2430141921d4c")])
def test_delete_note_with_valid_id(valid_login, id):
    response = requests.delete(f"{pytest.BASE_URL}/notes/{id}", headers=valid_login, verify=False)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Note successfully deleted"


"""
    -Delete notes with Invalid authorization.

    Returns:
    Throws validation error with status code 401

"""


@pytest.mark.sanity
@pytest.mark.regression
def test_delete_note_with_no_header():
    response = requests.delete(f"{pytest.BASE_URL}/notes/{id}", verify=False)
    assert response.status_code == 401
    assert response.json()["success"] is False
    assert response.json()["message"] == "No authentication token specified in x-auth-token header"


"""
    -Delete notes with id which is not present in database.

    Returns:
    Throws not found error with status code 404

"""


@pytest.mark.sanity
@pytest.mark.regression
@pytest.mark.parametrize("id", [("656cac5303e24301419218e6")])
def test_delete_note_with_id_not_in_database(valid_login, id):
    response = requests.delete(f"{pytest.BASE_URL}/notes/{id}", headers=valid_login, verify=False)
    assert response.status_code == 404
    assert response.json()["success"] is False
    assert response.json()["message"] == "No note was found with the provided ID, Maybe it was deleted"


"""
    -Delete notes with Valid authorization with invalid ID.

    Returns:
    Throws bad request with status code 400

"""


@pytest.mark.sanity
@pytest.mark.regression
def test_delete_note_with_invalid_id(valid_login):
    response = requests.delete(f"{pytest.BASE_URL}/notes/-1", headers=valid_login, verify=False)
    assert response.status_code == 400
    assert response.json()["success"] is False
    assert response.json()["message"] == "Note ID must be a valid ID"
