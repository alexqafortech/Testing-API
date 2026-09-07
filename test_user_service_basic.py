import pytest
from user_service import UserService

def test_register_with_invalid_email_raises_value_error():
    service = UserService("users.json")
    with pytest.raises(ValueError):
        service.register("not-an-email", "Password123")

def test_register_with_short_password_raises_value_error():
    service = UserService("users.json")
    with pytest.raises(ValueError):
        service.register("alice@example.com", "abc")