from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Page
from news.models import News


class DetailView(generic.DetailView):
    model = Page
    template_name = 'page/page.html'

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)

        context['slug'] = self.kwargs['slug']
        if context['slug'] == 'main':
            context['news_block'] = News.get_news_block
        if self.object.carousel:
            context['carousel_block'] = self.object.carousel.carouselslide_set.all()

        return context
