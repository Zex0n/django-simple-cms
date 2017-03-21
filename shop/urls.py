from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^shop/cart/$', views.CartView.as_view(), name='cart_list'),
    url(r'^shop/$', views.ListView.as_view(), name='list_all'),
    url(r'^shop/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^shop/(?P<slug_category>[-\w]+)/product/(?P<slug>[-\w]+)/$', views.ProductView.as_view(), name='product'),
]
