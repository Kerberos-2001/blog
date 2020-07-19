from .models import *
from django import forms
from django.forms import ModelForm


class blogForm(forms.Form):
        title = forms.CharField(max_length=150, widget = forms.TextInput(attrs={'class':'inpt', 'placeholder':'Title'}))
        body = forms.CharField(widget = forms.Textarea(attrs={'class':'inpt', 'placeholder':'Body'}))
        image = forms.ImageField(widget = forms.FileInput(attrs={'class':'inpt'}))