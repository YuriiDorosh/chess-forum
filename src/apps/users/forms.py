from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm

from users.models import User


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4", "placeholder": "Enter a name"})
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4", "placeholder": "Enter your last name"})
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4", "placeholder": "Enter a username"})
    )
    email = forms.CharField(
        widget=forms.EmailInput(attrs={"class": "form-control py-4", "placeholder": "Enter your email address"})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control py-4", "placeholder": "Password"})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control py-4", "placeholder": "Confirm password"})
    )

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")


class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control py-4", "placeholder": "Enter a username"})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={"class": "form-control py-4", "placeholder": "Password"})
    )

    class Meta:
        model = User
        fields = ["username", "password"]


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    # image = forms.ImageField(widget=forms.FileInput(attrs={"class": "custom-file-input"}), required=False)
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4", "readonly": True}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4", "readonly": True}))

    class Meta:
        model = User

        fields = ("first_name", "last_name", "photo", "username", "email")
