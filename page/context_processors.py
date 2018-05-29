from .models import Page, Menu, MenuSection, Carousel, CarouselSlide, Setting
from shop.models import Item
from news.models import  News
from django.core.cache import cache
from cart.views import Cart
from django.contrib.auth.models import User


from django.conf import settings

def context(request):
    cached_menus = cache.get(settings.MYMENU_CACHE_KEY)
    cached_carousel = cache.get(settings.CAROUSEL_CACHE_KEY)



    if cached_menus is not None:
        return cached_menus
    menus = Menu.objects.filter()
    context = {'menu': {}}
    for menu in menus:
        context['menu'][menu.slug] = menu
    cache.set(settings.MYMENU_CACHE_KEY, context, settings.CACHE_TIMEOUT)
    return context

    if cached_carousel is not None:
            return cached_carousel
    carousels = Carousel.objects.filter()
    context = {'carousel': {}}
    for carousel in carousels:
        context['carousel'][carousel.slug] = carousel
    cache.set(settings.CAROUSEL_CACHE_KEY, context, settings.CACHE_TIMEOUT)

    #context['offer']=Item.objects.filter(offer=True)

    return context






def offer(request):

    offer=Item.objects.filter(offer=True)

    return {"offer":offer}

def sitting(request):

    sitting=Setting.objects.first()


    return {"sitting":sitting}

def news(request):
    news=News.objects.all().order_by('-published_date')[:4]
    news_slider=News.objects.all().exclude(file_news__isnull=True).exclude(file_news='').order_by('-published_date')
    print(news_slider)
    return {"main_news":news, "news_slider":news_slider}

def count_cart(request):

    real_count_cart=0
    cart = Cart(request)

    for item in cart.list_items(lambda item: item.obj.title):

        if (request.user.is_authenticated):
            real_count_cart += item.obj.price_2 * item.quantity
        else:
            real_count_cart += item.obj.price_1 * item.quantity



    return {"real_count_cart":real_count_cart}




