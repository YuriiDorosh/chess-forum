from discussions.models import Discussion, Reply
from django import forms


class DiscussionForm(forms.ModelForm):
    class Meta:
        model = Discussion
        fields = ["title", "text", "image"]


# class ReplyForm(forms.ModelForm):
#     class Meta:
#         model = Reply
#         fields = ['text', 'image']

#     def clean(self):
#         cleaned_data = super().clean()
#         discussion = self.instance.discussion
#         if discussion.closed:
#             raise forms.ValidationError("This discussion is closed.")
#         return cleaned_data


class ReplyForm(forms.ModelForm):
    discussion_id = forms.CharField(widget=forms.HiddenInput())  # Додали поле discussion_id

    class Meta:
        model = Reply
        fields = ["text", "image"]

    def clean(self):
        cleaned_data = super().clean()
        discussion_id = cleaned_data.get("discussion_id")  # Отримали discussion_id з очищених даних
        try:
            discussion = Discussion.objects.get(pk=discussion_id)
            if discussion.closed:
                raise forms.ValidationError("This discussion is closed.")
        except Discussion.DoesNotExist:
            pass  # Обробляйте відсутність обговорення відповідним чином
        return cleaned_data
