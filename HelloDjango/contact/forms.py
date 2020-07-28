from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    """Форма обратной связи на странице проекта"""
    class Meta:
        model = Contact
        fields = ('name', 'phone', 'email')