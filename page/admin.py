from django.contrib import admin
from .models import Page, Menu, MenuSection
from grappelli.forms import GrappelliSortableHiddenMixin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import DraggableMPTTAdmin
from django import forms
from .forms import MenuAdminForm, PageAdminForm
from django.utils.translation import ugettext_lazy as _


class MenuSectionInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = MenuSection
    extra = 1
    sortable_field_name = "my_order"

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuSectionInline,]
    form = MenuAdminForm

admin.site.register(Menu, MenuAdmin)


class PageAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PageAdminForm

    class Media:
        js = [
            '//cdn.tinymce.com/4/tinymce.min.js',
            '/static/grappelli/tinymce_setup/tinymce4_setup.js',
        ]

    fieldsets = (
        (None, {
            'fields': ('parent', 'in_menus', 'title', 'menu_title', 'slug', 'meta_description', 'meta_keywords', 'login_required', 'content')
        }),
        (_('Расширенные настройки'), {
            'classes': ('collapse grp-collapse grp-closed',),
            'fields': ('page_type', 'redirect_url', 'application'),
        }),
    )

admin.site.register(Page, PageAdmin)