from common.factories import UserFactory
from common.test_utils import REDIRECT_302, TEST_USER_EMAIL, TEST_USER_PASSWORD, BaseTest
from django.test import Client

class UserLogoutTests(BaseTest):

    @classmethod
    def setUpTestData(cls):
        cls.user = UserFactory.create(email=TEST_USER_EMAIL, password=TEST_USER_PASSWORD)
        # force_login faster than .login
        Client().force_login(cls.user)

    def test_successful_user_logout(self):
        response = self.client.post("/registration/logout/")

        self.assertEqual(response.status_code, REDIRECT_302)
        self.assertEqual(response.url, '/registration/login')

