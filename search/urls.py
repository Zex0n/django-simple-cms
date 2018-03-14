from django.conf.urls import url
from . import views
from django.views.generic import TemplateView
urlpatterns = [
    url(r'^$', views.SearchListView.as_view(), {'slug': 'main'}, name='list_search'),
    # url(r'^page/goodpost/?$', TemplateView.as_view(template_name="page/good_post.html")),
    # url(r'^page/(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name='pagedetail'),
]