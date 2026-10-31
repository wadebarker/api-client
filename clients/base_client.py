import requests

from config.settings import BASE_URL, REQUEST_TIMEOUT


class BaseClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()

        self.session.headers.update({
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        })


    def get(self, endpoint):
        return self.session.get(
            url=f"{self.base_url}{endpoint}",
            timeout=REQUEST_TIMEOUT
        )


    def post(self, endpoint, json=None):
        return self.session.post(
            url=f"{self.base_url}{endpoint}",
            json=json,
            timeout=REQUEST_TIMEOUT
        )

    def close(self):
        self.session.close()
