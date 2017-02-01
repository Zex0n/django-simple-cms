from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.DetailView.as_view(), {'slug': 'main'}, name='index'),
    url(r'^page/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='pagedetail'),
]