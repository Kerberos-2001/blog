from .models import *
from django import forms


class Signup(forms.Form):
        first_name = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class':'inpt', 'placeholder':'First Name'}))
        last_name = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class':'inpt', 'placeholder':'Last Name'}))
        username = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class':'inpt', 'placeholder':'Username'}))
        email = forms.EmailField(max_length=150, widget = forms.EmailInput(attrs={'class':'inpt', 'placeholder':'email'}))
        password = forms.CharField(max_length=150, widget = forms.PasswordInput(attrs={'class':'inpt', 'placeholder':'Password'}))
        conform_password = forms.CharField(max_length=150, widget = forms.PasswordInput(attrs={'class':'inpt', 'placeholder':'Conform Password'}))
        number = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class':'inpt', 'placeholder':'Phone Number'}))
        address = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class':'inpt', 'placeholder':'Address'}))


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class':'inpt', 'placeholder':'Username'}))
    password = forms.CharField(max_length=150, widget = forms.PasswordInput(attrs={'class':'inpt', 'placeholder':'Password'}))