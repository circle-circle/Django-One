from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField()
    email = forms.EmailField(required=False, label='Your e-emal address')
    message = forms.CharField( widget=forms.Textarea )
