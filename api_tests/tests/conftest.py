import pytest
import requests
import uuid

@pytest.fixture(scope='session')
def base_url():
    return "http://localhost:8000"

@pytest.fixture(scope='session')
def api_session(base_url):
    """HTTP-сессия, используемая между тестами"""
    session = requests.Session()
    session.headers.update({
        "Content-Type": "application/json",
        "Accept": "application/json",
    })

    yield session

    session.close()

@pytest.fixture(scope='function')
def unique_user_data():
    """Создание уникальных данных для пользователей"""
    unique_user = uuid.uuid4().hex[:8]
    return {
        "email": f"test_{unique_user}@example.com",
        "username": f"user_{unique_user}",
        "password": "TestPass123!"
    }

@pytest.fixture(scope='session', autouse=True)
def check_api_available(base_url):
    try:
        response = requests.get(f"{base_url}/health", timeout=10)
        assert response.status_code == 200, f"API вернул {response.status_code}"
    except requests.exceptions.ConnectionError:
        pytest.exit("API недоступен. Запусти: docker compose up -d")



