from registration.forms import RegistrationForm
from django import forms

class UserProfileRegistrationForm(RegistrationForm):

    name = forms.CharField(label='Контактное лицо *', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    phone = forms.CharField(label='Телефон *', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    company_name = forms.CharField(label='Наименование компании *', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    inn = forms.CharField(label='ИНН *', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    kpp = forms.CharField(label='КПП', max_length=100,required=False, widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    orgn  = forms.CharField(label='ОГРН *', max_length=100,widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    bank  = forms.CharField(label='Наименование банка *', max_length=100,widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    bik  = forms.CharField(label='БИК *', max_length=100,widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    rs  = forms.CharField(label='Р/C *', max_length=100,widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    ks  = forms.CharField(label='К/C *', max_length=100,widget=forms.TextInput(attrs={'size': '40', 'class': 'form-control'}))
    city = forms.CharField(label='Город *', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    adres = forms.CharField(label='Адрес доставки', max_length=100,required=False, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))