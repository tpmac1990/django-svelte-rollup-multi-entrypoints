from common.factories import UserFactory
from common.test_utils import REDIRECT_302, TEST_USER_EMAIL, TEST_USER_PASSWORD, OK_200, BaseTest


class UserLoginTests(BaseTest):

    @classmethod
    def setUpTestData(cls):
        # cls.user = get_user_model().objects.create_user(email=TEST_USER_EMAIL, password=TEST_USER_PASSWORD)
        cls.user = UserFactory.create(email=TEST_USER_EMAIL, password=TEST_USER_PASSWORD)

    def test_successful_user_login(self):
        response = self.client.post("/registration/login/", data={"username": TEST_USER_EMAIL, "password": TEST_USER_PASSWORD})

        self.assertEqual(response.status_code, REDIRECT_302)
        self.assertEqual(response.url, '/htmx-lookup/films')

    def test_user_login__incorrect_email(self):
        response = self.client.post("/registration/login/", data={"username": "incorrect@mail.com", "password": TEST_USER_PASSWORD})
        
        # notify user that login was unsuccessful
        self.assertEqual(response.status_code, OK_200)
