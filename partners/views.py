from django.shortcuts import render
from django.views import generic


from .models import Regions, Dealers








class ListViewPartners(generic.ListView):
    model= Regions
    template_name = 'partners/list_partners.html'

    def get_context_data(self, *args, **kwargs):

            context = super(ListViewPartners, self).get_context_data(**kwargs)


            context['dealers'] = Dealers.objects.all()



            return context



class DetailView(generic.DetailView):
    template_name = 'partners/detail_partners.html'
    model = Dealers