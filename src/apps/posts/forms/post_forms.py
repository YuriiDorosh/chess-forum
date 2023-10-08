from django import forms
from posts.models.post import UserPost

class UserPostCreateForm(forms.ModelForm):
    image = forms.ImageField(required=False)  
    class Meta:
        model = UserPost
        fields = ["title", "game_link", "body", "image"] 

class UserPostUpdateForm(forms.ModelForm):
    image = forms.ImageField(required=False) 

    class Meta:
        model = UserPost
        fields = ["title", "game_link", "body", "image"]  
