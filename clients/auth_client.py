from clients.base_client import BaseClient


class AuthClient(BaseClient):

    def login(self, email, password):
        return self.post(
            endpoint='/api/auth/login',
            json={
                "email": email,
                "password": password,
            }
        )


    def register(self, email, password):
        return self.post(
            endpoint='/api/auth/register',
            json={
                "email": email,
                "password": password,
            }
        )


    def login_with_payload(self, payload):
        return self.post(
            endpoint='/api/auth/login',
            json=payload
        )


    def register_with_payload(self, payload):
        return self.post(
            endpoint='/api/auth/register',
            json=payload
        )