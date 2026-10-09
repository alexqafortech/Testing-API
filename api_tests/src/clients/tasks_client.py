from clients.base_client import BaseClient

class TasksClient(BaseClient):
    PREFIX  = "/api/v1/tasks"

    def create(self, title: str, **kwargs):
        payload = {"title": title}
        payload.update(kwargs)
        return self.post(self.PREFIX + "/", json=payload)

    def get_list(self, **params):
        return self.get(self.PREFIX + "/", params=params)

    def get_by_id(self, task_id: str):
        return self.get(self.PREFIX + "/" + task_id)

    def update(self, task_id: str, **fields):
        return self.put(self.PREFIX + "/" + task_id, json=fields)

    def delete(self, task_id: str):
        return super().delete(self.PREFIX + "/" + task_id)