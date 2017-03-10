from django.shortcuts import render
from django.views import generic


from .models import Regions, Dealers








class ListViewPartners(generic.ListView):
    model= Regions
    template_name = 'partners/list_partners.html'