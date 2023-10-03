from discussions.models.discussion import Discussion
from django import forms


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ["title", "text", "image"]
