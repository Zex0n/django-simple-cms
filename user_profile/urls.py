from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/$', views.edit_user, name="edit_user"),
]