from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^gallery/$', views.ListView.as_view(), name='list_all'),
    url(r'^gallery/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detail'),
]
