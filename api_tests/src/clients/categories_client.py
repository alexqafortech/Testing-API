from clients.base_client import BaseClient

class CategoriesClient(BaseClient):
    PREFIX = "/api/v1/categories"

    def create(self, payload, token, **kwargs):
        payload = payload
        payload.update(kwargs)
        return self.post(self.PREFIX + "/",
                         headers={"Authorization": f"Bearer {token}"}, json=payload)

    def get_list(self, token, **params):
        return self.get(self.PREFIX + "/",
                        headers={"Authorization": f"Bearer {token}"}, params=params)

    def get_by_id(self, category_id, token):
        return self.get(self.PREFIX + "/" + category_id,
                        headers={"Authorization": f"Bearer {token}"})

    def update(self, category_id, token, **fields):
        return self.put(self.PREFIX + "/" + category_id,
                        headers={"Authorization": f"Bearer {token}"}, json=fields)

    def delete(self, category_id, token):
        return super().delete(self.PREFIX + "/" + category_id,
                              headers={"Authorization": f"Bearer {token}"})

    def get_stats(self, category_id, token):
        return self.get(self.PREFIX + "/" + category_id + "/stats",
                        headers={"Authorization": f"Bearer {token}"})