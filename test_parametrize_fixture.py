import pytest
from user_service import UserService

@pytest.fixture
def user_service(tmp_path):
    storage = tmp_path / "users.json"
    storage.write_text("{}")
    return UserService(storage_path = storage)

@pytest.fixture(params = ["admin", "user", "guest"])
def user_with_role(request, user_service):
    role = request.param
    email = f"user_{role}@example.com"
    user_service.register(email, "Password123")
    return {"email": email, "role": role}

def test_any_role_can_login(user_service, user_with_role):
    user = user_service.login(user_with_role["email"], "Password123")
    assert user.email == user_with_role["email"]