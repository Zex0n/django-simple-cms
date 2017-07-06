from registration.forms import RegistrationForm
from django.forms import ModelForm
from .models import UserSettings
from django import forms

class UserRegForm(RegistrationForm):
    phone=forms.CharField(label='Телефон',max_length=200)