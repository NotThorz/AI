from django import forms


class YourForm(forms.Form):
    email = forms.EmailField()
