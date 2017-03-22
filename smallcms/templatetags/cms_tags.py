from django import template
from django.conf import settings
from django.template.loaders.app_directories import get_app_template_dirs
from django.template import Context
from django.template.library import SimpleNode
from django.template.loader import get_template
import os
from page.models import models
# from .models import Menu
# register = template.Library()
#
#
# class PlaceholderTag(template.Node):
#     def __init__(self, placeholder_name):
#         self.placeholder_name = placeholder_name
#
#     def render(self, context):
#         # TODO вывод менюшки с применением шаблона указанного в настройках
#         # t = template.loader.get_template('small_fragment.html')
#         # return t.render(Context({'var': obj}, autoescape=context.autoescape))
#         return self.placeholder_name
#
#
# def _db_index_placeholders(placeholder_list):
#     page_models.models.Placeholder.objects.all().delete()
#     for placeholder in placeholder_list:
#         p = Placeholder(title=placeholder)
#         p.save()
#
#
# def get_all_placeholders():
#     """
#     Returns a list of all placeholders names in all templates
#     """
#     template_dir_list = []
#     for each in get_app_template_dirs('templates'):
#         if settings.BASE_DIR in each:
#             template_dir_list.append(each)
#
#     placeholder_list = []
#     for each in (template_dir_list + settings.TEMPLATES[0]['DIRS']):
#         for fullpathdir, dirnames, filenames in os.walk(each):
#             for filename in filenames:
#                 placeholder_list += get_template_placeholder_list(os.path.join(fullpathdir, filename))
#
#     _db_index_placeholders(placeholder_list)
#
#     return placeholder_list
#
#
# def get_template_placeholder_list(string=None):
#     """
#     Returns a list of all placeholders names in template
#     """
#     t = get_template(string)
#     nodes = t.template.nodelist
#
#     variables = []
#     for node in nodes:
#
#         if SimpleNode is not None and isinstance(node, PlaceholderTag):
#             tag_name, placeholder_name = node.token.split_contents()
#             if tag_name == 'placeholder':
#                 variables.append(placeholder_name)
#
#     return variables
#
#
# @register.tag('placeholder')
# def do_placeholder(parser, token):
#     try:
#         # split_contents() knows not to split quoted strings.
#         tag_name, placeholder_name = token.split_contents()
#     except ValueError:
#         raise template.TemplateSyntaxError(
#             "%r tag requires a single argument" % token.contents.split()[0]
#         )
#     if placeholder_name[0] == placeholder_name[-1] and placeholder_name[0] in ('"', "'"):
#         raise template.TemplateSyntaxError(
#             "%r tag's argument should NOT be in quotes" % tag_name
#         )
#
#     return PlaceholderTag(placeholder_name)
#
#
# @register.simple_tag
# def placeholder(placeholder_name):
#     template_dir_list = []
#     for each in get_app_template_dirs('templates'):
#         if settings.BASE_DIR in each:
#             template_dir_list.append(each)
#
#     # template_list = []
#     placeholder_list = []
#     for each in (template_dir_list + settings.TEMPLATES[0]['DIRS']):
#         for dir, dirnames, filenames in os.walk(each):
#             for filename in filenames:
#                 # template_list.append(os.path.join(dir, filename))
#                 placeholder_list += _get_template_placeholder_list(os.path.join(dir, filename))
#
#     for a in placeholder_list:
#         print (a)
#
#     return placeholder_list
#
#
# def _get_template_placeholder_list(string=None):
#     """
#     Returns a list of all placeholders names
#     """
#     t = get_template(string)
#     template = t.template
#     nodes = template.nodelist
#
#     variables = []
#     for node in nodes:
#         if SimpleNode is not None and isinstance(node, SimpleNode):
#             tag_name, placeholder_name = node.token.split_contents()
#             if tag_name == 'placeholder':
#                 variables.append(placeholder_name)
#
#     return variables
