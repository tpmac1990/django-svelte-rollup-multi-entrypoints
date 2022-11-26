from django.test import TestCase

OK_200 = 200
PERMANENT_REDIRECT_301 = 301
REDIRECT_302 = 302
FORBIDDEN_403 = 403
NOT_FOUND_404 = 404

TEST_USER_EMAIL = 'test@mail.com' 
TEST_USER_PASSWORD = 'Mousebite321'


class BaseTest(TestCase):
    """
    Equal to using TestCase. 
    This provides a place to add additional reusable assert methods.
    """

    def assert_page_loading(self, path, status_code=OK_200, method="GET", data=None):
        if method == "GET":
            response = self.client.get(path=path)

        if method == "PUT":
            response = self.client.put(path=path, data=data)

        self.assertEqual(response.status_code, status_code)
        return response

