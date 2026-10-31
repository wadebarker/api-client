import pytest

from clients.auth_client import AuthClient
from data.user_factory import UserFactory


@pytest.fixture(scope="session")
def auth_client():
    client = AuthClient()

    yield client

    client.close()


@pytest.fixture
def create_new_valid_user():
    return UserFactory.valid_user()


@pytest.fixture
def registered_user(auth_client, create_new_valid_user):
    response = auth_client.register(
        email=create_new_valid_user['email'],
        password=create_new_valid_user['password'],
    )

    assert response.status_code == 201

    return {
        **create_new_valid_user,
        'id': response.json()['user']['id'],
    }


@pytest.fixture
def authorized_user(auth_client, registered_user):
    response = auth_client.login(
        email=registered_user['email'],
        password=registered_user['password'],
    )

    assert response.status_code == 200

    return {
        **registered_user,
        'accessToken': response.json()['accessToken'],
        'refreshToken': response.json()['refreshToken'],
    }
