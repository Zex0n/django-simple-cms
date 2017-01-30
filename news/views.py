from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.forms import ModelForm
from .models import News


class DetailView(generic.DetailView):
    model = News
    template_name = 'news/detail.html'


class ListView(generic.ListView):
    model= News
    template_name = 'news/all_list.html'

    def get_queryset(self):
        return News.objects.all()


    def get(self,request, *args, **kwargs):
        q = self.request.GET.get('per_page')
        t = self.request.COOKIES.get('per_page')
        if q:
            ListView.paginate_by = q
        elif t:
            ListView.paginate_by = t
        else:
            ListView.paginate_by = 5
        return super(ListView, self).get(request, *args, **kwargs)


    def render_to_response(self, context, **response_kwargs):
        response = super(ListView, self).render_to_response(context, **response_kwargs)
        response.set_cookie("per_page", ListView.paginate_by)
        return response


    def get_context_data(self, *args, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        context['per_page'] = ListView.paginate_by
        return context
