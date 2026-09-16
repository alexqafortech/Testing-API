# API Tests - Task Management API

Автотесты для [Task Management API](https://github.com/balakleeva/task_management_api)

## Требования
- Python 3.10+
- Docker и Docker Compose

## Быстрый старт

1. Склонируй репозиторий https://github.com/balakleeva/task_management_api
2. Создай файл .env
    ```bash
   cp .env.example .env
    ```
3. Подними API:
    ```bash
   docker compose up -d
   ```
4. Создай виртуальное окружение
    ```bash
   python -m venv venv
   ```
5. Установи библиотеки
    ```bash
   pip install -r requirements.txt
   ```

## Запуск тестов по группам

```bash
    pytest -v # Все тесты
    pytest -m auth -v # Тесты авторизации
    pytest -m negative -v # Негативные сценарии (невалидные данные)
    pytest -m tasks -v # Тесты связанные с задачами
    pytest -m contracts -v # Контрактные тесты
    pytest -m db -v # Тесты базы данных
```

## Структура проекта
- api_tests/src/clients/ - API-клиенты (BaseClient, AuthClient, TasksClient, CategoriesClient)
- api_tests/src/models/ - Pydantic-модели ответов API
- api_tests/src/db/ - Хелперы для работы с БД
- api_tests/src/config.py - Тесты с проверкой в БД
- api_tests/tests/api/ - API-тесты
- api_tests/tests/db/ - Тесты с проверкой в БД
- api_tests/tests/conftest.py - Общие фикстуры
