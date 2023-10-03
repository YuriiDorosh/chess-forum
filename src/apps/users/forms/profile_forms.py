from django import forms
from django.contrib.auth.forms import UserChangeForm

from users.models.user import User

class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    username = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4", "readonly": True}))
    email = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4", "readonly": True}))
    telegram_id = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))
    chess_profile_url = forms.URLField(widget=forms.TextInput(attrs={"class": "form-control py-4"}))

    class Meta:
        model = User
        fields = ("first_name", "last_name", "photo", "username", "email", "telegram_id", "chess_profile_url")