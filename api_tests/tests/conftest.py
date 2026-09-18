import pytest
import requests
import uuid

from clients.categories_client import CategoriesClient
from config import Config
from clients.auth_client import AuthClient
from clients.tasks_client import TasksClient

@pytest.fixture(scope = "session")
def config():
    return Config()

@pytest.fixture(scope='session')
def api_session():
    """HTTP-сессия, используемая между тестами"""
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json",
    })

    yield session

    session.close()

@pytest.fixture(scope='session', autouse=True)
def check_api_available(config):
    try:
        response = requests.get(f"{config.BASE_URL}/health", timeout=10)
        if response.status_code != 200:
            pytest.exit(f"API вернул {response.status_code}")
    except requests.exceptions.ConnectionError:
        pytest.exit("API недоступен. Запусти: docker compose up -d")

@pytest.fixture(scope='function')
def unique_user_data():
    """Создание уникальных данных для пользователей"""
    unique_user = uuid.uuid4().hex[:8]
    return {
        "email": f"test_{unique_user}@example.com",
        "username": f"user_{unique_user}",
        "password": "TestPass123!"
    }

@pytest.fixture(scope = "session")
def auth_client(api_session, config):
    client_auth = AuthClient(base_url = config.BASE_URL, session = api_session, timeout = config.API_TIMEOUT)
    return client_auth

@pytest.fixture(scope = "session")
def tasks_client(api_session, config):
    task = TasksClient(base_url = config.BASE_URL, session = api_session, timeout = config.API_TIMEOUT)
    return task

@pytest.fixture(scope = "session")
def category(api_session, config):
    res_category = CategoriesClient(base_url = config.BASE_URL, session = api_session, timeout = config.API_TIMEOUT)
    return res_category

@pytest.fixture(scope = "session")
def user_token(auth_client):
    unique_id = uuid.uuid4().hex[:8]
    user_data = {
        "email": f"session_{unique_id}@example.com",
        "username": f"session_{unique_id}",
        "password": "TestPass123!"
    }

    res_register = auth_client.register(**user_data)
    assert res_register.status_code == 201

    res_login = auth_client.login(username=user_data["username"], password=user_data["password"])
    assert res_login.status_code == 200
    return res_login.json()["access_token"]



