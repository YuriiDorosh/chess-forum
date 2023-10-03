from django import forms

from discussions.models.discussion import Discussion

class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ["title", "text", "image"]
