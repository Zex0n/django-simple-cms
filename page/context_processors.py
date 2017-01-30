from .models import Page, Menu, MenuSection
from django.core.cache import cache

from django.conf import settings

def context(request):
    cached_menus = cache.get(settings.MYMENU_CACHE_KEY)
    if cached_menus is not None:
        return cached_menus
    menus = Menu.objects.filter()
    context = {'menu': {}}
    for menu in menus:
        context['menu'][menu.slug] = menu
    cache.set(settings.MYMENU_CACHE_KEY, context, settings.MYMENU_CACHE_TIMEOUT)
    return context
