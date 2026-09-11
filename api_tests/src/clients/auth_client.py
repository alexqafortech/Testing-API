from src.clients.base_client import BaseClient

class AuthClient(BaseClient):

    PREFIX = "/api/v1/auth"

    def register(self, email=None, username=None, password=None, **kwargs):
        body = {}
        if email is not None:
            body["email"] = email
        if username is not None:
            body["username"] = username
        if password is not None:
            body["password"] = password

        body.update(kwargs)
        return self.post(self.PREFIX + "/register", json = body)

    def login(self, username, password):
        body = {
            "username": username,
            "password": password
        }
        return self.post(self.PREFIX + "/login", json = body)

    def get_me(self, token):
        return self.get(self.PREFIX + "/me", headers = {"Authorization": f"Bearer {token}"})