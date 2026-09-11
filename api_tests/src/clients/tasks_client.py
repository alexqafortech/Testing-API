from src.clients.base_client import BaseClient

class TasksClient(BaseClient):
    PREFIX  = "/api/v1/tasks"

    def create(self, title, token, **kwargs):
        payload = {"title": title}
        payload.update(kwargs)
        return self.post(self.PREFIX + "/",
                         headers = {"Authorization": f"Bearer {token}"}, json=payload)

    def get_list(self, token, **params):
        return self.get(self.PREFIX + "/",
                        headers = {"Authorization": f"Bearer {token}"}, params=params)

    def get_by_id(self, task_id, token):
        return self.get(self.PREFIX + "/" + task_id,
                        headers = {"Authorization": f"Bearer {token}"})

    def update(self, task_id, token, **fields):
        return self.put(self.PREFIX + "/" + task_id,
                        headers = {"Authorization": f"Bearer {token}"}, json=fields)

    def delete(self, task_id, token):
        return super().delete(self.PREFIX + "/" + task_id,
                              headers = {"Authorization": f"Bearer {token}"})