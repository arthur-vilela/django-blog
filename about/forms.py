from django import forms
from .models import CollaborateRequest


class CollaborateForm(forms.ModelForm):
    """
    Form to send user collaboration requests
    """
    class Meta:
        model = CollaborateRequest
        fields = ('name', 'email', 'message')