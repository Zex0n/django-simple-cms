from django.contrib import admin
from .models import Page, Menu, MenuSection, Carousel, CarouselSlide
from grappelli.forms import GrappelliSortableHiddenMixin
from django_mptt_admin.admin import DjangoMpttAdmin
from mptt.admin import DraggableMPTTAdmin
from django import forms
from .forms import MenuAdminForm, PageAdminForm, CarouselAdminForm
from django.utils.translation import ugettext_lazy as _


class MenuSectionInline(GrappelliSortableHiddenMixin, admin.TabularInline):
# class MenuSectionInline(admin.TabularInline):
    model = MenuSection
    extra = 1
    sortable_field_name = "my_order"
    # ordering = ("my_order",)

class MenuAdmin(admin.ModelAdmin):
    inlines = [MenuSectionInline,]
    form = MenuAdminForm

    fieldsets = (
        (None, {
            'fields': ('title',)
        }),
        (_('Расширенные настройки (не меняйте если не знаете для чего это нужно)'), {
            'classes': ('collapse grp-collapse grp-closed',),
            'fields': ('template', 'slug',),
        }),
    )

admin.site.register(Menu, MenuAdmin)


class PageAdmin(DraggableMPTTAdmin):
    prepopulated_fields = {"slug": ("title",)}
    form = PageAdminForm

    class Media:
        js = [
            # '//cdn.tinymce.com/4/tinymce.min.js',
            # '/static/grappelli/tinymce_setup/tinymce4_setup.js',
            '/static/admin/js/pageadmin.js',
        ]

    fieldsets = (
        (None, {
            'fields': ('parent', 'in_menus', 'title', 'menu_title', 'slug', 'meta_description', 'meta_keywords', 'login_required', 'content')
        }),
        (_('Расширенные настройки'), {
            'classes': ('collapse grp-collapse grp-closed',),
            'fields': ('page_type', 'redirect_url', 'carousel', 'application'),
        }),
    )

admin.site.register(Page, PageAdmin)


class CarouselSlideInline(admin.TabularInline):
    model = CarouselSlide
    extra = 3


class CarouselAdmin(admin.ModelAdmin):
    inlines = [CarouselSlideInline, ]
    # form = CarouselAdminForm

admin.site.register(Carousel, CarouselAdmin)