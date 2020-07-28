from urllib import request

from django import forms
from ckeditor.widgets import CKEditorWidget
from django.contrib.auth.models import User

from .models import Comment


class CommentForm(forms.ModelForm):
    """Форма Ответов на форуме"""
    class Meta:
        model = Comment
        fields = ('name', 'email', 'text', 'answer_for')

        widgets = {
            'text': CKEditorWidget(attrs={'id': 'f-text', 'required': '', 'placeholder': 'Ваше сообщение *'}),
            'name': forms.TextInput(attrs={'id': 'name', 'required': '', 'placeholder': 'Ваше имя *'}),
            'email': forms.TextInput(attrs={'id': 'email', 'required': '', 'placeholder': 'Email *'}),
            'answer_for': forms.TextInput(attrs={'id': 'answer_for', 'type': 'hidden'})
        }
#
# class CommentForm(forms.Form):
#     text = forms.CharField(widget=CKEditorWidget, label='')
#
#     text.widget.attrs.update({'id': 'post-text'})
