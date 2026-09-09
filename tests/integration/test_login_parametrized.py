import pytest
from user_service import UserService, InvalidCredentialsError

@pytest.fixture
def user_service_with_alice(tmp_path):
    storage = tmp_path / "users.json"
    storage.write_text("{}")
    service = UserService(storage_path = storage)
    service.register("alice@example.com", "Password123")
    return service

@pytest.mark.regression
@pytest.mark.auth
@pytest.mark.parametrize(
    "email, password",
    [
        pytest.param("alice@example.com", "WrongPass1", id = "wrong_password"),
        pytest.param("alice@example.com", "password123", id = "lowercase_password"),
        pytest.param("alice@example.com", "Password", id = "missing_digit"),
        pytest.param("ghost@example.com", "Password123", id = "unknown_email"),
        pytest.param("", "Password123", id = "empty_email"),
    ],
)
def test_login_with_invalid_credentials_raises(user_service_with_alice, email, password):
    with pytest.raises(InvalidCredentialsError):
        user_service_with_alice.login(email, password)