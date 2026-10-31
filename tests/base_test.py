import pytest

@pytest.mark.usefixtures("auth_client")
class BaseTest:

    @pytest.fixture(autouse=True)
    def setup(self, auth_client):
        self.auth_client = auth_client