from clients.base_client import BaseClient

class CategoriesClient(BaseClient):
    PREFIX = "/api/v1/categories"

    def create(self, payload, **kwargs):
        payload = payload
        payload.update(kwargs)
        return self.post(self.PREFIX + "/", json=payload)

    def get_list(self, **params):
        return self.get(self.PREFIX + "/", params=params)

    def get_by_id(self, category_id: str):
        return self.get(self.PREFIX + "/" + category_id)

    def update(self, category_id: str, **fields):
        return self.put(self.PREFIX + "/" + category_id, json=fields)

    def delete(self, category_id: str):
        return super().delete(self.PREFIX + "/" + category_id)

    def get_stats(self, category_id):
        return self.get(self.PREFIX + "/" + category_id + "/stats")