from django import forms
from .models import Menu
from django.contrib import admin
from django.conf import settings


class MenuAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MenuAdminForm, self).__init__(*args, **kwargs)
        self.fields['template'].choices += get_menu_templates()


def get_menu_templates():
    templates = list(getattr(settings, 'MENU_TEMPLATES', []))
    return templates


class PageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)
        self.fields['application'].choices += get_application_list()


def get_application_list():
    applications = list(getattr(settings, 'APPLICATION_LIST', []))
    return applications

