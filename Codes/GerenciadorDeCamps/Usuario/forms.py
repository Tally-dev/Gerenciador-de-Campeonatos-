from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django import forms

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2'
        )

class CustomUserLoginForm(LoginView):
    
    class Meta:
        model = User
        fields = (
            'username',
            'password'
        )