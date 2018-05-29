from django import forms
from django.contrib.auth.models import User

from shop.models import UserProfile





class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email',]


class RegisterForm1(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']


class RegisterForm2(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ['user']