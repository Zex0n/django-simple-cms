from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.core.mail import send_mail


from django import http
from django.views.generic import View

from .models import Page
from news.models import News
import requests


class DetailView(generic.DetailView):
    model = Page
    template_name = 'page/page.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)

        context['slug'] = self.kwargs['slug']
        if context['slug'] == 'main':
            context['news_block'] = News.get_news_block

        if self.object.carousel:
            context['carousel_block'] = self.object.carousel.carouselslide_set.all()

        return context

class SendMailCls(View):
    def post(self,request):

        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        recaptcha = request.POST.get('g-recaptcha-response')


        url = 'https://www.google.com/recaptcha/api/siteverify'
        payload = {"secret": "6LcVNlcUAAAAADTCtKuRHKWCN9Xy0kTELYWhncqh", "response": recaptcha}
        res = requests.post(url, data=payload)
        recaptcha_json = res.json()
        # print (recaptcha_json['success'])
        if recaptcha_json['success'] == True:
            send_message = '<h2>Сообщение с сайта CAIMAN </h2>'
            send_message = send_message+'<b>Имя:</b> '+name+'<br><br>'
            send_message = send_message+'<b>Телефон:</b> '+phone+'<br><br>'
            send_message = send_message+'<b>Сообщение:</b><br> '+message+'<br>'
            send_mail('Письмо с сайта CAIMAN', send_message, 'sendfromsite@caimanfishing.ru', ['ivan.tolkachev@gmail.com','orders@caimanfishing.ru'], fail_silently=False, auth_user=None, auth_password=None, connection=None, html_message=send_message)

            return HttpResponseRedirect('/page/goodpost')
        else:
            return HttpResponseRedirect('/page/errorpost')







