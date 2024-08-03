from django import forms
from .models import ContactUs

class SignUpForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'subject': forms.HiddenInput(attrs={'value': 'Investment Sign-Up'}),
        }
