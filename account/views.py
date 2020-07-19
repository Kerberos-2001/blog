from django.shortcuts import render, redirect
from .forms import *
from .models import *
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .utils import *
from django.contrib.auth import authenticate, login


AUTHER = get_user_model()

def SignUp(request):
    if request.method == 'POST':
        signup = Signup(request.POST)
        if signup.is_valid():
            clean_username(signup.cleaned_data['username'])
            clean(signup.cleaned_data['password'], signup.cleaned_data['conform_password'])
            
            USER = User()
            USERINFO = Auther()
            USER.username = signup.cleaned_data['username']
            USER.email = signup.cleaned_data['email']
            USER.first_name = signup.cleaned_data['first_name']
            USER.last_name = signup.cleaned_data['last_name']
            USER.set_password(signup.cleaned_data['password'])
            USER.save()

            USERINFO.number = signup.cleaned_data['number']
            USERINFO.address = signup.cleaned_data['address']
            USERINFO.conform_password = make_password(signup.cleaned_data['conform_password'])
            USERINFO.user = USER

            USERINFO.save()
        else:
            raise forms.ValidationError('This isnt a valid request')

    signup = Signup()
    context = {}
    context['form'] = signup
    return render(request, 'account/signup.html', context)


def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == 'POST':
        loginData = LoginForm(request.POST)
        if loginData.is_valid():
            username = loginData.cleaned_data['username']
            password = loginData.cleaned_data['password']
            print(username, password)
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('/')
            else:
                raise forms.ValidationError('Your Username and Password might be wrong')
        else:
            raise forms.ValidationError('This isnt a valid request')


    loginData = LoginForm()
    context = {}
    context['form'] = loginData
    return render(request, 'account/login.html', context)