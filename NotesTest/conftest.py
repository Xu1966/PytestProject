import pytest
import requests


# Assigned global variable
def pytest_configure():
    pytest.BASE_URL = "https://practice.expandtesting.com/notes/api"


# Setup fixture to authorize endpoints and teardown method by logging out
@pytest.fixture
def valid_login():
    data = {
        "email": "sujan@test.com",
        "password": "test123"
    }
    login_response = requests.post(f"{pytest.BASE_URL}/users/login", json=data, verify=False)
    login_token = login_response.json()["data"]["token"]
    headers = {
        'x-auth-token': f'{login_token}'
    }
    yield headers
    logout = requests.post(f"{pytest.BASE_URL}/users/logout", verify=False)
    print("User logout successful.")
