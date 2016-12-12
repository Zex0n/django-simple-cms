from django.contrib import admin
from .models import Page, Menu, MenuSection
from grappelli.forms import GrappelliSortableHiddenMixin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import DraggableMPTTAdmin
from django import forms


class MenuSectionInline(GrappelliSortableHiddenMixin, admin.TabularInline):
    model = MenuSection
    extra = 1
    sortable_field_name = "my_order"

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuSectionInline,]

admin.site.register(Menu, MenuAdmin)


class PageAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {"slug": ("title",)}

    class Media:
        js = [
            '//cdn.tinymce.com/4/tinymce.min.js',
            '/static/grappelli/tinymce_setup/tinymce4_setup.js',
        ]

admin.site.register(Page, PageAdmin)