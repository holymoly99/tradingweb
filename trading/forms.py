from django import forms
from .models import Write, Answer

from django_summernote.widgets import SummernoteWidget

class WriteForm(forms.ModelForm):
    class Meta:
        model = Write
        fields = ['subject', 'content', 'price', 'category', 'tmethod']

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        