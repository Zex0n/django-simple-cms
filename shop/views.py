from django.conf import settings
from django.shortcuts import render
from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.views import generic
from django.forms import ModelForm
from .models import Category, Item, Item_variation, Order, OrderItem, Status, UserProfile, TreeCash
from easycart import BaseCart, BaseItem
from cart.views import Cart
from django.contrib.auth.models import User
from django import forms
from django.views.generic import View
from django.core.mail import send_mail
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from datetime import datetime, timedelta
from django.utils import timezone
from operator import attrgetter
from django.views.decorators.csrf import csrf_exempt
from decimal import Decimal
from django.utils.text import slugify

class NoRegOrderForm(forms.Form):
    your_name = forms.CharField(label='Имя', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    company_name = forms.CharField(required=False, label='Наименование компании', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    phone = forms.CharField(label='Телефон', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    email = forms.EmailField(required=False, label='E-mail', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))
    dost_need = forms.BooleanField(required=False, label='Необходима доставка')
    dost_adres = forms.CharField(required=False, label='Адрес доставки', max_length=100, widget=forms.TextInput(attrs={'size':'40', 'class':'form-control'}))


class PostOrder(View):
    def post(self, request):

        cart = Cart(request)

        name = request.POST.get('your_name')
        company_name = request.POST.get('company_name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        dost_adres = request.POST.get('dost_adres')

        user_name = request.POST.get('user_name')

        dost_need = request.POST.get('dost_need')

        if(request.user.is_authenticated):
            send_message = '<h2>Заказ с сайта CAIMAN от пользователя '+user_name+' </h2>'
        else:
            send_message = '<h2>Анонимный заказ с сайта CAIMAN </h2>'

        send_message = send_message + '<b>Имя:</b> ' + name + '<br><br>'
        send_message = send_message + '<b>Наименование компании:</b> ' + company_name + '<br><br>'
        send_message = send_message + '<b>Телефон:</b> ' + phone + '<br><br>'
        send_message = send_message + '<b>E-mail:</b> ' + email + '<br><br>'
        if(dost_need): send_message = send_message + '<b>Необходима доставка - адрес доставки:</b> ' + dost_adres + '<br>'

        send_message = send_message + '<h2>Товары заказа</h2><table cellspacing="4" cellpadding="4"><tr><td align="center"><b>Наименование</b></td><td align="center"><b>Количество</b></td><td align="center" ><b>Цена</b></td><td align="center"><b>Сумма</b></td></tr>'
        total=0

        send_message = send_message + '<tr><td><h4>Товары в наличии</h4></td></tr>'





        if (request.user.is_authenticated):


            for item in cart.list_items(lambda item: item.obj.item.title):

                if (item.obj.stock == 1):
                    total += item.obj.price_2 * item.quantity
                    send_message = send_message + '<tr><td>'+item.obj.item.title+' '+item.obj.title+'</td><td align="center">'+str(item.quantity)+'</td><td align="center">'+str(item.obj.price_2)+' руб.</td><td align="center">'+str(item.obj.price_2*item.quantity)+'руб.</td></tr>'
        else:
            for item in cart.list_items(lambda item: item.obj.item.title):
                if (item.obj.stock == 1):
                    total += item.obj.price_1 * item.quantity
                    send_message = send_message + '<tr><td>'+item.obj.item.title+' '+item.obj.title+'</td><td align="center">'+str(item.quantity)+'</td><td align="center">'+str(item.obj.price_1)+' руб.</td><td align="center">'+str(item.obj.price_1*item.quantity)+'руб.</td></tr>'

        send_message = send_message + '<tr><td><h4>Товары в ожидании</h4></td></tr>'


        if (request.user.is_authenticated):



            for item in cart.list_items(lambda item: item.obj.item.title):
                if (item.obj.stock == 2):
                    total += item.obj.price_2 * item.quantity
                    send_message = send_message + '<tr><td>'+item.obj.item.title+' '+item.obj.title+'</td><td align="center">'+str(item.quantity)+'</td><td align="center">'+str(item.obj.price_2)+' руб.</td><td align="center">'+str(item.obj.price_2*item.quantity)+'руб.</td></tr>'
        else:
            for item in cart.list_items(lambda item: item.obj.item.title):
                if (item.obj.stock == 2):
                    total += item.obj.price_1 * item.quantity
                    send_message = send_message + '<tr><td>'+item.obj.item.title+' '+item.obj.title+'</td><td align="center">'+str(item.quantity)+'</td><td align="center">'+str(item.obj.price_1)+' руб.</td><td align="center">'+str(item.obj.price_1*item.quantity)+'руб.</td></tr>'






        send_message = send_message + '<tr><td colspan="4" align="right"><hr></td></tr>'
        send_message = send_message + '<tr><td colspan="4" align="right"><b>Итого: </b>'+str(total)+' руб. </td></tr></table>'
        #print(send_message)

        send_mail('Заказ с сайта CAIMAN', send_message, 'sendfromsite@caimanfishing.ru', ['ivan.tolkachev@gmail.com','orders@caimanfishing.ru'], fail_silently=False, auth_user='sendfromsite@caimanfishing.ru',auth_password='JmsdlfsldiJHMlsadfmKJ', connection=None, html_message=send_message)
        # send_mail('Заказ с сайта CAIMAN', send_message, 'sendfromsite@caimanfishing.ru', ['trumpk@gmail.com',], fail_silently=False, auth_user=None,auth_password=None, connection=None, html_message=send_message)
        #send_mail('Заказ с сайта CAIMAN', send_message, 'sendfromcaimansite@mail.ru', ['ivan.tolkachev@gmail.com'], fail_silently=False, auth_user=None,auth_password=None, connection=None, html_message=send_message)
        # Select default status for the order
        try:
            default_status = Status.objects.get(default_status=True)
        except:
            default_status = Status.objects.first()

        # create order in the database history
        order = Order(
            customer_id=request.user.pk,
            total_price=total,
            status=default_status
        )
        order.save()


        for item in cart.list_items(lambda item: item.obj.title):
            if (request.user.is_authenticated):
                order_item = OrderItem(
                    order = order,
                    item =  item.obj,
                    title = item.obj.item.title + ' ' + item.obj.title,
                    cols =  item.quantity,
                    price = item.obj.price_2,
                )
            else:
                order_item = OrderItem(
                    order = order,
                    item =  item.obj,
                    title = item.obj.item.title + ' ' + item.obj.title,
                    cols =  item.quantity,
                    price = item.obj.price_1,
                )
            order_item.save()

       # print(send_message)

        cart.empty()

        return HttpResponseRedirect('/shop/order-success')



class CartOrder(generic.ListView):
    template_name = 'shop/cart_order.html'

    def queryset(self):
        return super(CartOrder, self).queryset()

    def get_context_data(self, **kwargs):
        context = super(CartOrder, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        cart = Cart(request)

        # Создание заказа в базе
        # total = 0
        # for item in cart.list_items(lambda item: item.obj.title):
        #     total += item.obj.price_1 * item.quantity
        #
        # # Select default status for the order
        # try:
        #     default_status = Status.objects.get(default_status=True)
        # except:
        #     default_status = Status.objects.first()
        #
        # order = Order(
        #     customer_id=User.pk,
        #     total_price=total,
        #     status=default_status
        # )
        # order.save()

        # cart.empty()


        #for item in cart.list_items(lambda item: item.obj.title):

            #print(item.obj.item.title)

        return super(CartOrder, self).get(self, request, *args, **kwargs)


class CartView(generic.ListView):
    template_name = 'shop/cart.html'

    def queryset(self,request):
        return super(CartView, self).queryset()

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['form'] = NoRegOrderForm()
        context['userprofile']=UserProfile.objects.filter(user=self.request.user.id).first()
        return context


class DetailView(generic.DetailView):
    model = Category

    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['slug'] = self.kwargs['slug']
        current_category = Category.objects.get(slug=context['slug'])
        # print (current_category.get_family())
        # print (current_category.get_root())

        #Очистка кеша

        if TreeCash.objects.filter(cat_id=current_category).filter(created_date__lte=timezone.now() - timedelta(days=1)).count():
            cash=TreeCash.objects.filter(cat_id=current_category).filter(created_date__lte=timezone.now() - timedelta(days=1)).first()
            cash.delete()

        #cash = TreeCash.objects.get(cat_id=current_category)




        context['nodes'] = Category.objects.all()
        context['current_category'] = current_category
        context['current_category_root'] = current_category.get_root()
        # context['current_category_root'] = current_category.values_list('dinner__id', flat=True)
        context['object_list'] = Category.objects.filter(parent=current_category.pk)
        context['global_object_list'] = Category.objects.filter(level__lte=0)
        context['item_list'] = current_category.item_set.all()
        return context


class ListView(generic.ListView):
    model = Category

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


class SearchListView(generic.ListView):
    model = Item
    template_name = 'shop/category_detail.html'
    # paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(SearchListView, self).get_context_data(**kwargs)
        qs = Item.objects.all()
        keywords = self.request.GET.get('q')
        if keywords:
            query = SearchQuery(keywords)
            # vector = SearchVector('title', 'content')
            vector = SearchVector('title')
            qs = qs.annotate(search=vector).filter(search=query)

        context['item_list'] = qs
        context['object_list'] = {}

        context['nodes'] = Category.objects.all()

        return context

class TestApi(generic.TemplateView):
    template_name = 'shop/test_api.html'


@csrf_exempt
def capi(request):

    alphabet = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd', 'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i',
                'й': 'j', 'к': 'k', 'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r', 'с': 's', 'т': 't',
                'у': 'u', 'ф': 'f', 'х': 'kh', 'ц': 'ts', 'ч': 'ch', 'ш': 'sh', 'щ': 'shch', 'ы': 'i', 'э': 'e',
                'ю': 'yu',
                'я': 'ya'}

    if request.method == 'POST':

        try:
            id1c = request.POST['id1c']
            title = request.POST['title']
            in_stock = request.POST['in_stock']
            price_1 = request.POST['price_1']
            category = request.POST['category']

            if category == '':
                category = 999999999

            if int(in_stock) > 0:
                stock = 1
            else:
                stock = 2


        except:
            answer='Ошибка запроса'

        if(id1c!=''):
            count_this = Item_variation.objects.filter(vendor_code=id1c).count()

            if(count_this==0):

                slug=slugify(''.join(alphabet.get(w, w) for w in title.lower()))+'-'+id1c

                this_object = Item(title=title, meta_description=title,meta_keywords=title,slug=slug[:49])



                this_object.save()

                this_variation = Item_variation(title=" ",item=this_object, price_1=price_1, in_stock=in_stock, stock=stock, vendor_code =id1c)

                this_variation.save()

                cat = Category.objects.filter(code1c=category).first()
                if cat:
                    this_object.category.add(cat)

                answer = 'Product add'
            else:

                this_variation=Item_variation.objects.filter(vendor_code=id1c).first()
                this_variation.price_1=price_1
                this_variation.in_stock=in_stock
                this_variation.stock=stock
                this_variation.save()

                cat = Category.objects.filter(code1c=category).first()

                if cat:
                    this_object = this_variation.item
                    this_object.category.add(cat)

                answer = 'Product edited'

        else:
            answer = 'Параметр id1c должен быть задан'




    return HttpResponse(answer)
