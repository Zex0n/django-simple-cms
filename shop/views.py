from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.forms import ModelForm
from .models import Category, Item, Item_variation, Order, Status
from cart.views import Cart


import logging, logging.config
import sys


def CartOrder(request):
    cart = Cart(request)

    total = 0
    for item in cart.list_items(lambda item: item.obj.title):
        total += item.obj.price_1 * item.quantity

    # Select default status for the order
    try:
        default_status = Status.objects.get(default_status=True)
    except:
        default_status = Status.objects.first()

    order = Order (
        total_price = total,
        status = default_status

    )
    print(default_status)

    return render(request, 'shop/cart_order.html')


class CartView(generic.ListView):
    template_name = 'shop/cart.html'

    def queryset(self):
        return super(CartView, self).queryset()

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        return context


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
        context['current_category'] = get_object_or_404(Category, slug=context['slug_category'])
        context['current_product'] = get_object_or_404(Item, slug=context['slug'], status=True)
        context['item_variation'] = context['current_product'].item_variation_set.all()



        # context['object_list'] = current_category.get_children()
        # context['item_list'] = current_category.item_set.all()
        return context