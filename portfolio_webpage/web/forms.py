from multiprocessing.resource_tracker import register

from  django import forms
from .models import Contact
from django import template

def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'phone', 'subject', 'message']
