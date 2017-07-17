from registration.backends.simple.views import RegistrationView
from .forms import UserProfileRegistrationForm
from shop.models import UserProfile
from django.core.mail import send_mail


class MyRegistrationView(RegistrationView):

    form_class = UserProfileRegistrationForm

    def register(self, form_class):
        new_user = super(MyRegistrationView, self).register(form_class)
        name = form_class.cleaned_data['name']
        phone = form_class.cleaned_data['phone']
        company_name = form_class.cleaned_data['company_name']
        inn = form_class.cleaned_data['inn']
        city = form_class.cleaned_data['city']
        adres = form_class.cleaned_data['adres']

        send_message = '<h2>Регистрация нового пользователя на сайте CAIMAN </h2>'
        send_message = send_message + '<b>Имя:</b> ' + name + '<br><br>'
        send_message = send_message + '<b>Наименование компании:</b> ' + company_name + '<br><br>'
        send_message = send_message + '<b>Телефон:</b> ' + phone + '<br><br>'
        send_message = send_message + '<b>Город:</b> ' + city + '<br><br>'
        send_message = send_message + '<b>Адрес доставки:</b> ' + adres + '<br>'


        print(send_message)

        send_mail('Регистрация нового пользователя', send_message, 'sendfromsite@caimanfishing.ru',
                  ['ivan.tolkachev@gmail.com', 'orders@caimanfishing.ru'], fail_silently=False, auth_user=None,
                  auth_password=None, connection=None, html_message=send_message)





        new_profile = UserProfile.objects.create(user=new_user, name=name, phone=phone, company_name=company_name, inn=inn, city=city, adres=adres)
        new_profile.save()
        return new_user


