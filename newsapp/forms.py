from django import forms
from .models import *





class SubscriberForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = "__all__"
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email...'
            }),
        }



class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter name...'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email...'
            }),
           
            'message': forms.Textarea(attrs={
                "class": 'form-control',
                'placeholder': 'Enter your message...'
            }),
        }