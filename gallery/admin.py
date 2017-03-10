from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Item, Category
from embed_video.admin import AdminVideoMixin


class ItemInline(AdminVideoMixin, admin.TabularInline):
    model = Item
    extra = 3


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ItemInline, ]

admin.site.register(Category, CategoryAdmin)