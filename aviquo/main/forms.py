"""Forms"""
from django import forms

from .models import Tag, User, Waitlist, Forum
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class TagFilterForm(forms.Form):
    """Tag filter"""

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )


class EditProfileForm(forms.ModelForm):
    """Edit profile"""

    class Meta:
        """First name, last name, username, email, bio, pfp"""

        model = User
        fields = [
            "first_name",
            "last_name",
            "username",
            "email",
            "bio",
            "profile_image",
        ]


class AddWaitlistForm(forms.ModelForm):
    """Add to waitlist"""

    class Meta:
        """Email"""

        model = Waitlist
        fields = ["email"]


class AddForumForm(forms.ModelForm):
    """Add forum post"""

    class Meta:
        """Topic, description"""

        model = Forum
        fields = ["topic", "description"]


class CustomUserCreationForm(UserCreationForm):
    """Create user"""

    def __init__(self, *args, **kwargs):
        """Form for user"""

        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields["password1"].widget.attrs["oninput"] = "check"
        self.fields["password2"].widget.attrs["oninput"] = "check"
        self.fields["username"].widget.attrs["minlength"] = "3"
        self.fields["username"].widget.attrs["maxlength"] = "24"
        self.fields["password1"].widget.attrs["minlength"] = "8"
        self.fields["password1"].widget.attrs["maxlength"] = "32"
        self.fields["password1"].widget.attrs[
            "pattern"
        ] = "^(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).+$"

    email = forms.EmailField(required=True)  # Make the email field required

    class Meta:
        """Fields + email"""

        model = User
        fields = tuple(UserCreationForm.Meta.fields) + ("email",)


class CustomAuthForm(UserCreationForm):
    """Login form"""

    def __init__(self, *args, **kwargs):
        """Remove pass fields"""
        super(CustomAuthForm, self).__init__(*args, **kwargs)
        self.fields.pop("password1")
        self.fields.pop("password2")

    class Meta:
        """Username and pass"""

        model = User
        fields = ["username", "password"]
