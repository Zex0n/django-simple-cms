from django.conf.urls import url
from . import views


urlpatterns = [
    # url(r'^news/([\w-]+)$', views.ListView.as_view(), name='list'),
    url(r'^news/$', views.ListView.as_view(), name='list_all'),
    url(r'^news/(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
]
