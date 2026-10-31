import pytest

from tests.base_test import BaseTest


class TestLogin(BaseTest):

    def test_login_success(self, registered_user):
        response = self.auth_client.login(
            email=registered_user["email"],
            password=registered_user["password"]
        )

        assert response.status_code == 200

        body = response.json()

        assert body["user"]["email"] == registered_user["email"]
        assert body["user"]["id"] == registered_user["id"]

        assert isinstance(body["accessToken"], str)
        assert isinstance(body["refreshToken"], str)

        assert body["accessToken"]
        assert body["refreshToken"]


    def test_login_wrong_password(self, registered_user):
        response = self.auth_client.login(
            email=registered_user["email"],
            password="WrongPassword123"
        )

        assert response.status_code == 401

    def test_login_unknown_email(self, create_new_valid_user):
        response = self.auth_client.login(
            email=create_new_valid_user["email"],
            password=create_new_valid_user["password"]
        )

        assert response.status_code == 401

    @pytest.mark.parametrize(
        "payload",
        [
            {"email": "test@gmail.com"},
            {"password": "Test12345@@"},
            {},
            {"email": None, "password": "Test12345@@"},
            {"email": "test@gmail.com", "password": None},
            {"email": 123456, "password": "Test12345@@"}
        ],
        ids=[
            "missing_password",
            "missing_email",
            "empty_body",
            "null_email",
            "null_password",
            "invalid_email_type"
        ]
    )
    def test_login_invalid_payload(self, payload):
        response = self.auth_client.login_with_payload(
            payload
        )

        assert response.status_code == 400
        assert response.json()["statusCode"] == 400

    def test_login_missing_password_error(self):
        response = self.auth_client.login_with_payload({
            "email": "test@gmail.com"
        })

        assert response.status_code == 400

        body = response.json()

        assert body["statusCode"] == 400
        assert body["error"] == "Bad Request"
        assert isinstance(body["message"], list)

        assert "password must be a string" in body["message"]