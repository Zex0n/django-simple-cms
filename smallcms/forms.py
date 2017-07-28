from registration.forms import RegistrationForm
from django import forms

class UserProfileRegistrationForm(RegistrationForm):

    name = forms.CharField(label='Контактное лицо', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    phone = forms.CharField(label='Телефон', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    company_name = forms.CharField(label='Наименование компании', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    inn = forms.CharField(label='ИНН', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    city = forms.CharField(label='Город', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    adres = forms.CharField(label='Адрес доставки', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))