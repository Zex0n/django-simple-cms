from django import template
register = template.Library()

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
def sub(value, arg):

    return int(value) - int(arg)

def div(value, arg):

    return int(value) / int(arg)

