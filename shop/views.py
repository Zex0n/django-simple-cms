from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.forms import ModelForm
from .models import Category, Item


class DetailView(generic.DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']
        current_category = Category.objects.get(slug=context['slug'])
        context['object_list'] = current_category.get_children()
        context['item_list'] = current_category.item_set.all()
        return context


class ListView(generic.ListView):
    model= Category

    def get_context_data(self, **kwargs):
        context = super(ListView, self).get_context_data(**kwargs)
        # context['slug'] = self.kwargs['slug']
        context['object_list'] = Category.objects.filter(level__lte=0)

        return context


class ProductView(generic.DetailView):
    model = Item

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['slug_category'] = self.kwargs['slug_category']
        context['slug'] = self.kwargs['slug']
        context['current_category'] = Category.objects.get(slug=context['slug_category'])
        context['current_product'] = Item.objects.get(slug=context['slug'])

        # context['object_list'] = current_category.get_children()
        # context['item_list'] = current_category.item_set.all()
        return context