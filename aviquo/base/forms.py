"""
Forms for the Base app
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField

from .models import User


class RegisterForm(UserCreationForm):
    """Form for registration"""

    email = forms.EmailField(max_length=128, help_text="Required")

    def __init__(self, *args, **kwargs) -> None:
        """Create the form"""

        super(RegisterForm, self).__init__(self, *args, **kwargs)

    class Meta:
        """Meta class for the ModelForm"""

        model = User
        fields = ("username", "email", "password1", "password2")
        field_classes = {"username": UsernameField}
