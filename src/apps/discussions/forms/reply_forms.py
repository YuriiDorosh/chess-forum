from discussions.models.discussion import Discussion
from discussions.models.reply import Reply
from django import forms


class ReplyForm(forms.ModelForm):
    discussion_id = forms.CharField(widget=forms.HiddenInput())

    class Meta:
        model = Reply
        fields = ["text", "image"]

    def clean(self):
        cleaned_data = super().clean()
        discussion_id = cleaned_data.get("discussion_id")
        try:
            discussion = Discussion.objects.get(pk=discussion_id)
            if not discussion:
                raise forms.ValidationError("Discussion doesn't exist.")
            if discussion.closed:
                raise forms.ValidationError("This discussion is closed.")
        except Discussion.DoesNotExist as e:
            raise forms.ValidationError(f"Discussion doesn't exist: {e}")
        return cleaned_data
