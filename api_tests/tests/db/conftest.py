import pytest
from db.helpers import DBHelper

@pytest.fixture(scope="function")
def db_cursor(db_connection):
    """Курсор для выполнения запросов. Новый на каждый тест."""
    cursor = db_connection.cursor()
    yield cursor
    db_connection.rollback()
    cursor.close()

@pytest.fixture(scope="session")
def db(db_connection):
    return DBHelper(db_connection)