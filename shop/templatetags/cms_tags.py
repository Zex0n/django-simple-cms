from django import template
register = template.Library()
from decimal import *

from django.contrib.auth.models import User as auth_user

from shop.models import Category, TreeCash, UserProfile, Item, Discount

@register.filter()
def add_class(field, css):
   return field.as_widget(attrs={"class":css})


@register.simple_tag(takes_context = True)
def cookie(context, cookie_name): # could feed in additional argument to use as default value
    request = context['request']
    result = request.COOKIES.get('t'+str(cookie_name),'') # I use blank as default value
    if result=='':
        result='0'
    return result


@register.simple_tag()
def mult(value, arg):
    return int(value) * int(arg)


@register.simple_tag()
def get_discount_all(mass, user):

    count=0


    for node in mass:

        disc_level = UserProfile.objects.filter(user=user.pk).first().member_type


        product = node.obj

        if product.stock==1:
            if disc_level == 0:
                get_product_percent = Item.objects.filter(id=product.item.id).first().discount_system.level1
            if disc_level == 1:
                get_product_percent = Item.objects.filter(id=product.item.id).first().discount_system.level2
            if disc_level == 2:
                get_product_percent = Item.objects.filter(id=product.item.id).first().discount_system.level3

            count = count + (product.price_2-(product.price_2*get_product_percent/100))*node.quantity

    return round(count,2)


@register.simple_tag()
def get_discount_dif(mass, user):

    count=0

    count_2=0


    for node in mass:

        disc_level = UserProfile.objects.filter(user=user.pk).first().member_type

        product = node.obj

        if product.stock == 1:

            if disc_level == 0:
                get_product_percent = Item.objects.filter(id=product.item.id).first().discount_system.level1
            if disc_level == 1:
                get_product_percent = Item.objects.filter(id=product.item.id).first().discount_system.level2
            if disc_level == 2:
                get_product_percent = Item.objects.filter(id=product.item.id).first().discount_system.level3

            count_2 = count_2 + product.price_2*node.quantity

    for node in mass:

        disc_level = UserProfile.objects.filter(user=user.pk).first().member_type

        product = node.obj
        if product.stock == 1:
            if disc_level == 0:
                get_product_percent = Item.objects.filter(id=product.item.id).first().discount_system.level1
            if disc_level == 1:
                get_product_percent = Item.objects.filter(id=product.item.id).first().discount_system.level2
            if disc_level == 2:
                get_product_percent = Item.objects.filter(id=product.item.id).first().discount_system.level3

            count = count + (product.price_2-(product.price_2*get_product_percent/100))*node.quantity

    return round(count_2-count,2)




@register.simple_tag()
def get_discount(value, user, item):

    disc_level=UserProfile.objects.filter(user=user.pk).first().member_type

    try:
        if disc_level==0:
            get_product_percent=Item.objects.filter(id=item.id).first().discount_system.level1
        if disc_level==1:
            get_product_percent=Item.objects.filter(id=item.id).first().discount_system.level2
        if disc_level==2:
            get_product_percent=Item.objects.filter(id=item.id).first().discount_system.level3
    except:
        get_product_percent=0

    disc_price=value-value*get_product_percent/100

    if (disc_price == value):
        return str(disc_price)+' &#8381; <br><br>'
    else:
        return '<b>' + str(round(disc_price,2)) + '</b> &#8381; <br><small> <s>' + str(value) + ' &#8381; </s></small>'



@register.simple_tag()
def get_discount_summ(value, user, item, quantity):

    disc_level=UserProfile.objects.filter(user=user.pk).first().member_type

    if disc_level==0:
        get_product_percent=Item.objects.filter(id=item.id).first().discount_system.level1
    if disc_level==1:
        get_product_percent=Item.objects.filter(id=item.id).first().discount_system.level2
    if disc_level==2:
        get_product_percent=Item.objects.filter(id=item.id).first().discount_system.level3

    disc_price=(value-value*get_product_percent/100)*quantity

    return round(disc_price,2)


@register.simple_tag
def last_child(node):

    count=TreeCash.objects.filter(cat_id=node)
    if not count:
        last_count=recursive_list(node)
        cash=TreeCash(cat_id=node,elm_cols=last_count)
        cash.save()
    else:
        last_count=count.first().elm_cols


    #last_count = recursive_list(node)

    return last_count
    # children = node.get_children()
    # if children:
    #     return list(children)[-1]
    # else:
    #     return ''

def recursive_list(nodes):
    children = nodes.get_children()
    if children:
        count = 0
        for node in children:
            count = count + recursive_list(node)
        return count
    else:
        return nodes.item_set.count()


@register.simple_tag
def min_child(node, is_anonymous):

    if is_anonymous:

        if TreeCash.objects.filter(cat_id=node).exclude(price_from_anon=None).count():
            min = TreeCash.objects.filter(cat_id=node).first().price_from_anon
            last_count=min
        else:
            last_count = recursive_list_min(node, is_anonymous)
            cash = TreeCash.objects.filter(cat_id=node).first()
            cash.price_from_anon=last_count
            cash.save()
    else:
        if TreeCash.objects.filter(cat_id=node).exclude(price_from=None).count():
            min = TreeCash.objects.filter(cat_id=node).first().price_from
            last_count=min
        else:
            last_count = recursive_list_min(node, is_anonymous)
            cash = TreeCash.objects.filter(cat_id=node).first()
            cash.price_from=last_count
            cash.save()


    last_count = last_count
    return last_count

def recursive_list_min(nodes, is_anonymous):
    children = nodes.get_children()
    if children:
        min = 0
        for node in children:
            current_min = recursive_list_min(node, is_anonymous)

            if (min != 0) and (int(current_min) < int(min)):
                min = current_min
            elif (min == 0):
                min = current_min

        return min
    else:
        min = 0
        for node in nodes.item_set.all():
            # print ('------------------------', user.is_anonymous)

            try:
                iterated_price = node.item_variation_set.first().price_1 if is_anonymous else node.item_variation_set.first().price_2
                if (iterated_price == '') or (not iterated_price):
                    iterated_price = 0

                if (min != 0) and (int(iterated_price) < int(min)):
                    min = iterated_price
                elif (min == 0):
                    min = iterated_price
            except:
                print("Переменная не определана")


        return int(min)


@register.simple_tag
def max_child(node, is_anonymous):

    if is_anonymous:

        if TreeCash.objects.filter(cat_id=node).exclude(price_to_anon=None).count():
            min = TreeCash.objects.filter(cat_id=node).first().price_to_anon
            last_count=min
        else:
            last_count = recursive_list_max(node, is_anonymous)



            cash = TreeCash.objects.filter(cat_id=node).first()
            cash.price_to_anon=last_count
            cash.save()
    else:
        if TreeCash.objects.filter(cat_id=node).exclude(price_to=None).count():
            min = TreeCash.objects.filter(cat_id=node).first().price_to
            last_count=min

        else:
            last_count = recursive_list_max(node, is_anonymous)

            print(last_count)

            cash = TreeCash.objects.filter(cat_id=node).first()
            cash.price_to=last_count
            cash.save()

    last_count = last_count
    return last_count

def recursive_list_max(nodes, is_anonymous):
    children = nodes.get_children()
    if children:
        max = 0
        for node in children:
            try:
                current_max = recursive_list_max(node, is_anonymous)
                if (max != 0) and (int(current_max) > int(max)):
                    max = current_max
                elif (max == 0):
                    max = current_max
            except:
                print("Переменная не определена")
        return max
    else:
        max = 0
        for node in nodes.item_set.all():

            try:
                iterated_price = node.item_variation_set.first().price_1 if is_anonymous else node.item_variation_set.first().price_2
                if (iterated_price == '') or (not iterated_price):
                    iterated_price = 0

                if (max != 0) and (int(iterated_price) > int(max)):
                    max = iterated_price
                elif (max == 0):
                    max = iterated_price
            except:
                print("Переменная не определена")
        return int(max)



@register.simple_tag()
def sub(value, arg):
    return int(value) - int(arg)


def div(value, arg):
    return int(value) / int(arg)

