from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profile/$', views.edit_user, name="edit_user"),
    url(r'^orders_history/$', views.orders_history, name="orders_history"),
    url(r'^user_register/$', views.user_register, name="user_register"),
]