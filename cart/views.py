from django.shortcuts import render
from easycart import BaseCart, BaseItem

# We assume here that you've already defined your item model
# in a separate app named "catalog".
from shop.models import Item_variation


class Cart(BaseCart):

    def get_queryset(self, pks):
        item_vars = Item_variation.objects.filter(pk__in=pks)
        for item_var in item_vars:
            item_var.price = item_var.price_1

        return item_vars
