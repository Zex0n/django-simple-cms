from registration.backends.simple.views import RegistrationView
from .forms import UserProfileRegistrationForm
from shop.models import UserProfile
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.shortcuts import redirect

# from django.dispatch import receiver
# from django.db.models.signals import pre_save
# from django.contrib.auth.models import User

import sys

#
# @receiver(pre_save, sender=User)
# def set_new_user_inactive(sender, instance, **kwargs):
#     if instance._state.adding is True:
#         instance.is_active = False





class MyRegistrationView(RegistrationView):

    form_class = UserProfileRegistrationForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        name = form_class.cleaned_data['name']
        phone = form_class.cleaned_data['phone']
        company_name = form_class.cleaned_data['company_name']
        inn = form_class.cleaned_data['inn']
        kpp = inn = form_class.cleaned_data['kpp']
        orgn = inn = form_class.cleaned_data['orgn']
        bank = inn = form_class.cleaned_data['bank']
        bik = inn = form_class.cleaned_data['bik']
        rs = inn = form_class.cleaned_data['rs']
        ks = inn = form_class.cleaned_data['ks']
        city = form_class.cleaned_data['city']
        adres = form_class.cleaned_data['adres']

        send_message = '<h2>Регистрация нового пользователя на сайте CAIMAN </h2>'
        send_message = send_message + '<b>Имя пользователя:</b> ' + new_user.username + '<br><br>'
        send_message = send_message + '<b>Имя:</b> ' + name + '<br><br>'
        send_message = send_message + '<b>Наименование компании:</b> ' + company_name + '<br><br>'
        send_message = send_message + '<b>Телефон:</b> ' + phone + '<br><br>'
        send_message = send_message + '<b>Город:</b> ' + city + '<br><br>'
        send_message = send_message + '<b>Адрес доставки:</b> ' + adres + '<br>'


        #print(send_message)

        # try:
        #     send_mail('Регистрация нового пользователя', send_message, 'sendfromsite@caimanfishing.ru',
        #           ['ivan.tolkachev@gmail.com', 'orders@caimanfishing.ru'], fail_silently=False, auth_user=None,
        #           auth_password=None, connection=None, html_message=send_message)
        # except Exception:
        #     print("Nosend")







        new_profile = UserProfile.objects.create(user=new_user, name=name, phone=phone, company_name=company_name, inn=inn, kpp=kpp, orgn=orgn, bank=bank, bik=bik, rs=rs,ks=ks, city=city, adres=adres)
        new_profile.save()


        #print(new_user.pk)

        user = User.objects.get(pk=new_user.pk)
        user.is_active = False
        user.save()

        redirect('/shop/')

        print('adASADaD')

        redirect('/shop/')

        #return new_user
        return redirect('/shop/')

