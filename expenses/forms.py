from django import forms
from . import models


class FeedbackForm(forms.Form):
    subject = forms.CharField(max_length=200)
    request_response_from_sysop = forms.BooleanField(
        required=False, help_text="We provide answers in less than 5 years."
    )
    content = forms.CharField(widget=forms.Textarea, label="Your content here:")
    email = forms.EmailField()
    rating = forms.IntegerField(min_value=1, max_value=5)


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        exclude = ("user",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = (
            "content",
            "is_todo",
        )
