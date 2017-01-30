from django import forms
from .models import Menu, MenuSection
from django.contrib import admin
from django.conf import settings
# from smallcms.templatetags.cms_tags import get_all_placeholders
# from multiselectfield import MultiSelectFormField


class MenuAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MenuAdminForm, self).__init__(*args, **kwargs)
        self.fields['template'].choices += get_menu_templates()
        # self.fields['placeholder'] = MultiSelectFormField(
        #     choices=get_all_placeholders()
        # )
        # TODO сделать переиндексирование в базу плейсхолдеров при входе в админку а в модели выборку плейсхолдеров только из базы
    def save(self, *args, **kwargs):
        MenuSection.objects.rebuild()
        return super(MenuAdminForm, self).save(*args, **kwargs)


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

