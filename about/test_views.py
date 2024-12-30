from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from .models import About
from .forms import CollaborateForm


class TestAboutView(TestCase):

    def setUp(self):
        """Creates about me content"""
        self.about = About(
            title="About title", content="Collab request", profile_image="placeholder"
        )
        self.about.save()

    def test_render_about_page_with_collaboration_form(self):
        """Verifies get request for about me containing a collaboration form"""
        response = self.client.get(reverse("about"))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"About title", response.content)
        self.assertIn(b"Collab request", response.content)
        self.assertIn(b"placeholder", response.content)
        self.assertIsInstance(response.context["collaborate_form"], CollaborateForm)

    def test_successful_collaboration_request_submission(self):
        """Test for a user requesting a collaboration"""
        post_data = {
            "name": "test name",
            "email": "test@email.com",
            "message": "test message",
        }
        response = self.client.post(reverse("about"), post_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b"Collaboration request received! I endeavor to respond within 2 working days.",
            response.content,
        )
