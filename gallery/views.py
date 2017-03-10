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

class ListView(generic.ListView):
    model= Category

