from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^list/$', views.ListViewPartners.as_view(), name='list_partners'),


    #url(r'^/map/$', views.ListViewMap.as_view(), name='list_partnesr_map'),

    #url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='partner_detail'),


]