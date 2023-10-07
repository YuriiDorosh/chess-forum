from django import forms

class ReplyLikeForm(forms.Form):
    reply_id = forms.UUIDField(widget=forms.HiddenInput())
