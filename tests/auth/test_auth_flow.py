import pytest

from tests.base_test import BaseTest


# Тест на на флоу регистрации: сделали новую учётку и проверили что под её кредами можно войти
class TestAuthFlow(BaseTest):

    def test_register_then_login(self, create_new_valid_user):

        # Шаг 1. Регистрация новой учётки
        register_response = self.auth_client.register(
            **create_new_valid_user
        )

        assert register_response.status_code == 201

        register_body = register_response.json()

        user_id = register_body["user"]["id"]

        # Шаг 2. Авторизация под созданной учёткой
        login_response = self.auth_client.login(
            **create_new_valid_user
        )

        assert login_response.status_code == 200

        login_body = login_response.json()

        # Шаг 3. Проверка пользователя
        assert login_body["user"]["id"] == user_id

        assert (
            login_body["user"]["email"]
            == create_new_valid_user["email"]
        )

        # Шаг 4. Проверка токенов
        assert login_body["accessToken"]
        assert login_body["refreshToken"]