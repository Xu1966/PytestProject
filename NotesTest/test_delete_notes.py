import pytest
import requests


@pytest.mark.parametrize("id", [("656cac5303e24301419218e6")])
def test_delete_note_with_valid_id(valid_login, id):
    headers = {'x-auth-token': f'{valid_login}'}
    response = requests.delete(f"{pytest.BASE_URL}/notes/{id}", headers=headers, verify=False)
    assert response.status_code == 200
    assert response.json()["success"] is True
    assert response.json()["message"] == "Note successfully deleted"


def test_delete_note_with_no_header():
    response = requests.delete(f"{pytest.BASE_URL}/notes/{id}", verify=False)
    assert response.status_code == 401
    assert response.json()["success"] is False
    assert response.json()["message"] == "No authentication token specified in x-auth-token header"


@pytest.mark.parametrize("id", [("656cac5303e24301419218e6")])
def test_delete_note_with_id_not_in_database(valid_login, id):
    headers = {'x-auth-token': f'{valid_login}'}
    response = requests.delete(f"{pytest.BASE_URL}/notes/{id}", headers=headers, verify=False)
    assert response.status_code == 404
    assert response.json()["success"] is False
    assert response.json()["message"] == "No note was found with the provided ID, Maybe it was deleted"


def test_delete_note_with_invalid_id(valid_login):
    headers = {'x-auth-token': f'{valid_login}'}
    response = requests.delete(f"{pytest.BASE_URL}/notes/-1", headers=headers, verify=False)
    assert response.status_code == 400
    assert response.json()["success"] is False
    assert response.json()["message"] == "Note ID must be a valid ID"
