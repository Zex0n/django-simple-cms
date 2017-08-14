from django import template
register = template.Library()

@register.filter()
def add_class(field, css):
   return field.as_widget(attrs={"class":css})


@register.simple_tag()
def mult(value, arg):

    return int(value) * int(arg)

@register.simple_tag()
def sub(value, arg):

    return int(value) - int(arg)

def div(value, arg):

    return int(value) / int(arg)

