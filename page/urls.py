from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
urlpatterns = [


    url(r'^$', views.DetailView.as_view(), {'slug': 'main'}, name='index'),

    url(r'^page/goodpost/?$', TemplateView.as_view(template_name="page/good_post.html")),
    url(r'^page/errorpost/?$', TemplateView.as_view(template_name="page/error_post.html")),
    url(r'^page/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='pagedetail'),
    url(r'^page/sendmymail/?$', views.SendMailCls.as_view(), name='sendmymail'),


]