import pytest
from api_tests.tests.conftest import unique_user_data

@pytest.fixture
def url_register():
    return "/api/v1/auth/register"

@pytest.fixture
def url_login():
    return "/api/v1/auth/login"

@pytest.mark.auth
def test_register_new_user(auth_client, unique_user_data):
    res = auth_client.register(**unique_user_data)
    assert res.status_code == 201
    res_data = res.json()['user']
    assert "email" in res_data

@pytest.mark.negative
def test_register_duplicate_email(auth_client, unique_user_data):
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
    first_response = auth_client.register(**original_data)
    assert first_response.status_code == 201
    second_response = auth_client.register(**duplicate_email)
    assert second_response.status_code == 409

@pytest.mark.auth
def test_login_success(auth_client, unique_user_data):
    res_register = auth_client.register(**unique_user_data)
    assert res_register.status_code == 201

    res_login = auth_client.login(unique_user_data['username'], unique_user_data['password'])
    data = res_login.json()
    assert "access_token" in data

@pytest.mark.negative
def test_login_wrong_password(auth_client, unique_user_data):
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
    res_register = auth_client.register(**user_register)
    assert res_register.status_code == 201
    res_login = auth_client.login(user_login['username'], user_login['password'])
    assert res_login.status_code == 401

@pytest.mark.negative
def test_login_nonexistent_user(auth_client, unique_user_data):
    res_login = auth_client.login(unique_user_data['username'], unique_user_data['password'])
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
def test_register_validation(user, expected_status_code, auth_client):
    res = auth_client.register(**user)
    assert res.status_code == expected_status_code, f"Payload: {user}, получили {res.status_code}"
