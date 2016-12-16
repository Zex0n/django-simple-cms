from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Page


class IndexView(generic.ListView):
    template_name = 'page/page.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Page.objects.all()


class DetailView(generic.DetailView):
    model = Page
    template_name = 'page/detail.html'


class ResultsView(generic.DetailView):
    model = Page
    template_name = 'page/results.html'


