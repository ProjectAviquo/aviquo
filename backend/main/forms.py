from django import forms

from .models import Tag, User, Waitlist, Forum
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class TagFilterForm(forms.Form):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

class AddWaitlistForm(forms.ModelForm):
    class Meta:
        model = Waitlist
        fields = ["email"]

class AddForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ["topic", "description"]
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Make the email field required
    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ("email",)

class CustomAuthForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomAuthForm, self).__init__(*args, **kwargs)
        self.fields.pop('password1')
        self.fields.pop('password2')

    class Meta:
        model = User
        fields = ["username", "password"]