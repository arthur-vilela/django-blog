from django.test import TestCase
from .forms import CollaborateForm


class TestCollaborateForm(TestCase):

    def test_form_is_valid(self):
        """Test for all fields"""
        form = CollaborateForm(
            {"name": "Arthur", "email": "test@test.com", "message": "Hello!"}
        )
        self.assertTrue(form.is_valid(), msg="Form is not valid")

    def test_name_field_is_valid(self):
        """Test for the name field"""
        form = CollaborateForm({"name": "", "email": "test@test.com", "body": "Hello!"})
        self.assertFalse(
            form.is_valid(), msg="Name was not provided, but the form is valid"
        )

    def test_email_field_is_valid(self):
        """Test for the email field"""
        form = CollaborateForm({"name": "Arthur", "email": ".com", "body": "Hello!"})
        self.assertFalse(
            form.is_valid(), msg="Email was not provided, but the form is valid"
        )

    def test_body_field_is_valid(self):
        """Test for the body field"""
        form = CollaborateForm({"name": "Arthur", "email": "test@test.com", "body": ""})
        self.assertFalse(
        form.is_valid(), msg="Message was not provided, but the form is valid"
        )               