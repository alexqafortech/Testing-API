import pytest
from api_tests.tests.conftest import unique_user_data
from models.task import TaskResponse

@pytest.mark.tasks
def test_create_task(auth_client, unique_user_data, tasks_client):
    res_register = auth_client.register(**unique_user_data)
    assert res_register.status_code == 201

    res_login = auth_client.login(unique_user_data['username'], unique_user_data['password'])
    assert res_login.status_code == 200
    token = res_login.json()['access_token']
    res_create_task = tasks_client.create("Buy milk", token)
    assert res_create_task.status_code == 201
    task = TaskResponse.model_validate(res_create_task.json())
    assert task.title == "Buy milk"
    assert task.status == "TODO"

@pytest.mark.tasks
def test_get_task_by_id(auth_client, unique_user_data, tasks_client):

    res_register = auth_client.register(**unique_user_data)
    assert res_register.status_code == 201

    res_login = auth_client.login(unique_user_data['username'], unique_user_data['password'])
    assert res_login.status_code == 200
    token = res_login.json()['access_token']

    res_create_task = tasks_client.create("Buy milk", token)
    task_id = res_create_task.json()['id']

    res_get_task = tasks_client.get_by_id(task_id, token)
    assert res_get_task.status_code == 200
    task = TaskResponse.model_validate(res_get_task.json())
    assert task.title == "Buy milk"
    assert task.status == "TODO"

@pytest.mark.tasks
def test_get_tasks_list(auth_client, unique_user_data, tasks_client):
    res_register = auth_client.register(**unique_user_data)
    assert res_register.status_code == 201

    res_login = auth_client.login(unique_user_data['username'], unique_user_data['password'])
    assert res_login.status_code == 200
    token = res_login.json()['access_token']

    res_create_first_task = tasks_client.create("test1", token)
    assert res_create_first_task.status_code == 201
    res_create_second_task = tasks_client.create("test2", token)
    assert res_create_second_task.status_code == 201

    res_list = tasks_client.get_list(token)
    count_of_items = res_list.json()['items']
    assert len(count_of_items) == 2

@pytest.mark.tasks
def test_delete_task(auth_client, unique_user_data, tasks_client):
    res_register = auth_client.register(**unique_user_data)
    assert res_register.status_code == 201

    res_login = auth_client.login(unique_user_data['username'], unique_user_data['password'])
    assert res_login.status_code == 200
    token = res_login.json()['access_token']

    res_create_task = tasks_client.create("test1", token)
    task_id = res_create_task.json()['id']

    res_delete_task = tasks_client.delete(task_id, token)
    assert res_delete_task.status_code == 204

    res_get_task = tasks_client.get_by_id(task_id, token)
    assert res_get_task.status_code == 404





