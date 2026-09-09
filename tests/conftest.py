"""
Корневой conftest для всех тестов.

Добавляет директорию src/ в sys.path, чтобы тесты могли
импортировать модули как 'from user_service import ...'
без указания полного пути.
"""

import sys
from pathlib import Path



# Добавляем src/ в sys.path
SRC_DIR = Path(__file__).parent.parent / "src"
sys.path.insert(0, str(SRC_DIR))

import pytest
from user_service import UserService

@pytest.fixture
def storage_file(tmp_path):
    """Временный JSON-файл с пустым словарём пользователей."""
    path = tmp_path / "users.json"
    path.write_text("{}")
    return path

@pytest.fixture
def user_service(storage_file):
    """Чистый UserService с пустым хранилищем."""
    return UserService(storage_path = storage_file)

@pytest.fixture
def valid_credentials():
    """Эталонные валидные данные для регистрации."""
    return {"email": "alice@example.com", "password": "Password123"}

@pytest.fixture
def registered_user(user_service, valid_credentials):
    """Готовый зарегистрированный пользователь"""
    user_service.register(**valid_credentials)
    return valid_credentials
