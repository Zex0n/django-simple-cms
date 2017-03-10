from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Item, Category


class ItemInline(admin.TabularInline):
    model = Item
    extra = 3


class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ItemInline, ]

admin.site.register(Category, CategoryAdmin)