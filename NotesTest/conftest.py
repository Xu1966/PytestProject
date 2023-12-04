import pytest
import requests


def pytest_configure():
    pytest.BASE_URL = "https://practice.expandtesting.com/notes/api"


@pytest.fixture
def valid_login():
    data = {
        "email": "sujan@test.com",
        "password": "test123"
    }
    login_response = requests.post(f"{pytest.BASE_URL}/users/login", data, verify=False)
    login_data = login_response.json().get("data")
    login_token = login_data.get("token")
    yield login_token
    logout = requests.post(f"{pytest.BASE_URL}/users/logout", verify=False)
    print("User logout successful.")
