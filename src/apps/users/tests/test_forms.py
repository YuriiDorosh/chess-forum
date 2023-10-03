from django.test import TestCase
from users.forms.authentication_forms import RegistrationForm


class RegistrationFormTest(TestCase):
    def test_registration_form_valid_data(self):
        form_data = {
            "first_name": "first name",
            "last_name": "last name",
            "username": "testuser",
            "email": "test@example.com",
            "password1": "securepassword",
            "password2": "securepassword",
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_registration_form_invalid_data(self):
        form_data = {
            "first_name": "first name",
            "last_name": "last name",
            "username": "testuser",
            "email": "invalid-email",
            "password1": "securepassword",
            "password2": "securepassword",
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
