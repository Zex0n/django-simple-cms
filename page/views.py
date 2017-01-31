from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Page
from news.models import News


class IndexView(generic.ListView):
    model = Page
    template_name = 'page/mainpage.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['news_block'] = News.get_news_block
        return context

class DetailView(generic.DetailView):
    model = Page
    template_name = 'page/page.html'


class ResultsView(generic.DetailView):
    model = Page
    template_name = 'page/results.html'
