from django.contrib.auth import get_user_model
from common.test_utils import BaseTest, REDIRECT_302
from registration.forms import RegisterForm


class UserRegistrationTests(BaseTest):

    def test_register_user(self):
        data = {"email": "fake@mail.com", "password1": "Bagpipes123", "password2": "Bagpipes123"}
        form = RegisterForm(data=data)

        is_valid = form.is_valid()

        self.assertEqual(is_valid, True)
        self.assertEqual(form.cleaned_data, data)
        self.assertEqual(form.errors, {})

        form.save()

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 1)
        self.assertEqual(users.first().email, data['email'])

    def test_register_user__no_data_passed(self):
        data = {}
        form = RegisterForm(data=data)

        is_valid = form.is_valid()

        self.assertEqual(is_valid, False)
        errors = {'email': ['This field is required.'], 'password1': ['This field is required.'], 'password2': ['This field is required.']}
        self.assertEqual(form.errors, errors)

        users = get_user_model().objects.all()
        self.assertEqual(users.count(), 0)

    def test_register_user__incorrect_email_format(self):
        data = {"email": "fakemail.com", "password1": "Bagpipes123", "password2": "Bagpipes123"}
        form = RegisterForm(data=data)

        is_valid = form.is_valid()

        self.assertEqual(is_valid, False)
        self.assertEqual(form.errors['email'], ['Enter a valid email address.'])

    def test_register_user__different_passwords(self):
        data = {"email": "fake@mail.com", "password1": "Bagpipes123", "password2": "bagpipes123"}
        form = RegisterForm(data=data)

        is_valid = form.is_valid()

        self.assertEqual(is_valid, False)
        self.assertEqual(form.errors['password2'], ['The two password fields didn’t match.'])

    def test_registration_page_redirects_to_login_on_success(self):
        response = self.client.post("/registration/register/", data={"email": "fake@mail.com", "password1": "Bagpipes123", "password2": "Bagpipes123"})
        
        self.assertEqual(response.status_code, REDIRECT_302)
        self.assertEqual(response.url, '/registration/login/')

    def test_registration_page_renders_missing_email_error(self):
        response = self.client.post("/registration/register/", data={})

        self.assertContains(response, 'This field is required.')

    def test_registration_page_renders_mismatching_password_error(self):
        response = self.client.post("/registration/register/", data={"email": "fake@mail.com", "password1": "Bagpipes123", "password2": "bagpipes123"})

        self.assertContains(response, 'The two password fields didn’t match.')



