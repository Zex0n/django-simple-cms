from django import template
register = template.Library()
from decimal import *

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


@register.simple_tag
def last_child(node):
    last_count = recursive_list(node)
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
    last_count = recursive_list_min(node, is_anonymous)
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

            iterated_price = node.item_variation_set.first().price_1 if is_anonymous else node.item_variation_set.first().price_2
            if (iterated_price == '') or (not iterated_price):
                iterated_price = 0

            if (min != 0) and (int(iterated_price) < int(min)):
                min = iterated_price
            elif (min == 0):
                min = iterated_price

        return int(min)


@register.simple_tag
def max_child(node, is_anonymous):
    last_count = recursive_list_max(node, is_anonymous)
    return last_count

def recursive_list_max(nodes, is_anonymous):
    children = nodes.get_children()
    if children:
        max = 0
        for node in children:
            current_max = recursive_list_max(node, is_anonymous)
            if (max != 0) and (int(current_max) > int(max)):
                max = current_max
            elif (max == 0):
                max = current_max
        return max
    else:
        max = 0
        for node in nodes.item_set.all():
            iterated_price = node.item_variation_set.first().price_1 if is_anonymous else node.item_variation_set.first().price_2
            if (iterated_price == '') or (not iterated_price):
                iterated_price = 0

            if (max != 0) and (int(iterated_price) > int(max)):
                max = iterated_price
            elif (max == 0):
                max = iterated_price
        return int(max)


@register.simple_tag()
def sub(value, arg):
    return int(value) - int(arg)


def div(value, arg):
    return int(value) / int(arg)

