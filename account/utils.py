from django.contrib.auth import get_user_model
from django import forms
AUTHER = get_user_model()

def clean_username(Susername):
    if AUTHER.objects.filter(username = Susername).exists():
        raise forms.ValidationError(Susername+' Username is already taken')
    return Susername

def clean(password, conpassword):
    if password != conpassword:
        raise forms.ValidationError("Password didn't match")