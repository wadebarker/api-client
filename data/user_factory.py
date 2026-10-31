from faker import Faker

fake = Faker()


class UserFactory:
    @staticmethod
    def valid_user():
        return {
            'email': fake.email(),
            'password': fake.password(length=10),
        }

    @staticmethod
    def invalid_email_cases():
        return [
            ('short email', 'a@b.r'),
            ('without @', 'domain.ru'),
            ('without domain', 'vad_zv@mail'),
            ('empty email', ''),
        ]


    @staticmethod
    def invalid_password_cases():
        return [
            ('empty password', ''),
            ('too short password', fake.password(length=5)),
            ('too long password', fake.password(length=51)),
        ]