from multiprocessing.resource_tracker import register

from  django import forms
from .models import Contact
from django import template



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
