from django import forms
from posts.models.post import UserPost


class UserPostCreateForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ["title", "game_link", "body"]


class UserPostUpdateForm(forms.ModelForm):
    class Meta:
        model = UserPost
        fields = ["title", "game_link", "body"]
