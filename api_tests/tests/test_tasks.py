import pytest
from api_tests.tests.conftest import unique_user_data

@pytest.mark.tasks
def test_create_task(auth_client, unique_user_data, tasks_client):
    res_register = auth_client.register(**unique_user_data)
    assert res_register.status_code == 201

    res_login = auth_client.login(unique_user_data['username'], unique_user_data['password'])
    assert res_login.status_code == 200
    token = res_login.json()['access_token']

    res_create_task = tasks_client.create("test", token)

@pytest.mark.tasks
def test_get_task_by_id(auth_client, unique_user_data, tasks_client):

    res_register = auth_client.register(**unique_user_data)
    assert res_register.status_code == 201

    res_login = auth_client.login(unique_user_data['username'], unique_user_data['password'])
    assert res_login.status_code == 200
    token = res_login.json()['access_token']

    res_create_task = tasks_client.create("test", token)
    task_id = res_create_task.json()['id']

    res_get_task = tasks_client.get_by_id(task_id, token)
    assert res_get_task.status_code == 200
    title = res_get_task.json()['title']
    assert title is not None

@pytest.mark.tasks
def test_get_tasks_list(auth_client, unique_user_data, tasks_client):
    res_register = auth_client.register(**unique_user_data)
    assert res_register.status_code == 201

    res_login = auth_client.login(unique_user_data['username'], unique_user_data['password'])
    assert res_login.status_code == 200
    token = res_login.json()['access_token']

    res_create_first_task = tasks_client.create("test1", token)
    res_create_second_task = tasks_client.create("test2", token)

    res_list = tasks_client.get_list(token)
    list = res_list.json()['items']
    assert len(list) == 2

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

    res_get_task = tasks_client.get_by_id(task_id, token)
    assert res_get_task.status_code == 404





