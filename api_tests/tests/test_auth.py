import pytest
import requests
from api_tests.tests.conftest import unique_user_data


@pytest.fixture
def url_register():
    return "/api/v1/auth/register"

@pytest.fixture
def url_login():
    return "/api/v1/auth/login"

@pytest.mark.auth
def test_register_new_user(base_url, url_register, unique_user_data):
    res = requests.post(f"{base_url}{url_register}", json=unique_user_data)
    assert res.status_code == 201
    res_data = res.json()['user']
    assert "email" in res_data

@pytest.mark.negative
def test_register_duplicate_email(base_url, url_register, unique_user_data):
    original_data = {
        "email": unique_user_data['email'],
        "password": unique_user_data['password'],
        "username": unique_user_data['username']
    }
    duplicate_email = {
        "email": original_data['email'],
        "password": original_data['password'],
        "username": "second_name"
    }
    first_response = requests.post(f"{base_url}{url_register}", json=original_data)
    assert first_response.status_code == 201
    second_response = requests.post(f"{base_url}{url_register}", json=duplicate_email)
    assert second_response.status_code == 409

@pytest.mark.auth
def test_login_success(base_url, url_register, url_login, unique_user_data):
    user = {
        "email": unique_user_data['email'],
        "password": unique_user_data['password'],
        "username": unique_user_data['username']
    }
    res_register = requests.post(f"{base_url}{url_register}", json=user)
    assert res_register.status_code == 201

    res_login = requests.post(f"{base_url}{url_login}", json=user)
    data = res_login.json()
    assert "access_token" in data

@pytest.mark.negative
def test_login_wrong_password(base_url, url_register, url_login, unique_user_data):
    user_register = {
        "email": unique_user_data['email'],
        "password": "TestPass123!",
        "username": unique_user_data['username']
    }
    user_login = {
        "email": user_register['email'],
        "password": "WrongPass1!",
        "username": user_register['username']
    }
    res_register = requests.post(f"{base_url}{url_register}", json=user_register)
    assert res_register.status_code == 201
    res_login = requests.post(f"{base_url}{url_login}", json=user_login)
    assert res_login.status_code == 401

@pytest.mark.negative
def test_login_nonexistent_user(base_url, url_login, unique_user_data):
    res_login = requests.post(f"{base_url}{url_login}", json=unique_user_data)
    assert res_login.status_code == 401

@pytest.mark.negative
@pytest.mark.parametrize("user, expected_status_code",[
    pytest.param(
      {
          "email": "",
          "password": "TestPass123!",
          "username": "TestUser"
      },
      422,
      id = "empty_email"
    ),
    pytest.param(
        {
          "email": "not-an-email",
          "password": "TestPass123!",
          "username": "TestUser"
        },
        422,
        id = "invalid_email"
    ),
    pytest.param(
        {
          "email": "test@example.com",
          "password": "TestPass123!",
        },
        422,
        id = "missing_username"
    ),
    pytest.param(
        {
            "email": "test@example.com",
            "username": "TestUser"
        },
        422,
        id = "missing_password"
    ),
    pytest.param(
        {},
        422,
        id = "empty_body"
    )
])
def test_register_validation(user, expected_status_code, base_url, url_register):
    res = requests.post(f"{base_url}{url_register}", json=user)
    assert res.status_code == expected_status_code, f"Payload: {user}, получили {res.status_code}"
