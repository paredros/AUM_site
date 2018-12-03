from django import forms
from aum.models import ContactWebpage, NewsletterContact


class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=30, required=True, label='Your Name',
                    widget=forms.TextInput(attrs={'placeholder': 'Enter Your Name'}))
    email = forms.EmailField(max_length=254, required=True, label='Email',
                    widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email Address'}))
    subject = forms.CharField(max_length=254, required=True, label='Subject',
                    widget=forms.TextInput(attrs={'placeholder': 'Enter a Subject for your Message'}))
    message = forms.CharField(
        max_length=2000,
        required=True,
        label='Message',
        widget=forms.Textarea(attrs={'placeholder': 'Write your Message'})
    )

    class Meta:
        model = ContactWebpage
        fields = ['name', 'email', 'subject', 'message']


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField(max_length=254, required=True, label="", help_text="",
                             widget=forms.TextInput(attrs={'placeholder': 'Enter Your Email Address'}))

    class Meta:
        model = NewsletterContact
        fields = ['email']
