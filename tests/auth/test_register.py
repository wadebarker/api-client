import pytest

from data.user_factory import UserFactory
from tests.base_test import BaseTest


class TestRegister(BaseTest):

    def test_register_success(self, create_new_valid_user):
        response = self.auth_client.register(
            email = create_new_valid_user['email'],
            password = create_new_valid_user['password']
        )

        assert response.status_code == 201

        body = response.json()

        assert body['user']['email'] == create_new_valid_user['email']
        assert isinstance(body['user']['id'], int)

        assert isinstance(body['accessToken'], str)
        assert len(body['accessToken']) > 0

        assert isinstance(body['refreshToken'], str)
        assert len(body['refreshToken']) > 0


    def test_register_duplicate_email(self, create_new_valid_user):
        success_register = self.auth_client.register(**create_new_valid_user)

        assert success_register.status_code == 201

        repeat_register_response = self.auth_client.register(**create_new_valid_user)

        assert repeat_register_response.status_code == 400


    @pytest.mark.parametrize(
        'case_email, email',
        UserFactory.invalid_email_cases()
    )
    def test_register_invalid_email(self, case_email, email):
        response = self.auth_client.register(
            email=email,
            password='Qwerty123',
        )

        assert response.status_code == 400



    @pytest.mark.parametrize(
        'case_password, password',
        UserFactory.invalid_password_cases()
    )
    def test_register_invalid_password(self, case_password, password):
        user = UserFactory.valid_user()

        response = self.auth_client.register(
            email=user['email'],
            password=password,
        )

        assert response.status_code == 400