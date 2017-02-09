from django import forms
from .models import MenuSection, Carousel
from django.contrib import admin
from django.conf import settings
# from smallcms.templatetags.cms_tags import get_all_placeholders
# from multiselectfield import MultiSelectFormField


# Menu admin forms
class MenuAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MenuAdminForm, self).__init__(*args, **kwargs)
        self.fields['template'].choices += get_menu_templates()

    def save(self, *args, **kwargs):
        MenuSection.objects.rebuild()
        return super(MenuAdminForm, self).save(*args, **kwargs)


def get_menu_templates():
    templates = list(getattr(settings, 'MENU_TEMPLATES', []))
    return templates


# Carousel admin forms
class CarouselAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(CarouselAdminForm, self).__init__(*args, **kwargs)
        self.fields['template'].choices += get_carousel_templates()
        Carousel.full_clean()

def get_carousel_templates():
    templates = list(getattr(settings, 'CAROUSEL_TEMPLATES', []))
    return templates


# Page admin forms
class PageAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PageAdminForm, self).__init__(*args, **kwargs)
        self.fields['application'].choices += get_application_list()


def get_application_list():
    applications = list(getattr(settings, 'APPLICATION_LIST', []))
    return applications
