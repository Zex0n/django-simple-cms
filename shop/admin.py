from django.contrib import admin
from django_mptt_admin.admin import DjangoMpttAdmin
from .models import Item, Item_variation, Item_image, Category
import nested_admin


class Item_imageInline(nested_admin.NestedTabularInline):
    model = Item_image
    extra = 1
    ordering = ['num', ]


class Item_variationInline(nested_admin.NestedStackedInline):
    model = Item_variation
    inlines = [Item_imageInline,]
    extra = 1
    ordering = ['num',]


class ItemAdmin(nested_admin.NestedModelAdmin):
    #inlines = [Item_variationInline,]
    inlines = [Item_variationInline,]
    prepopulated_fields = {"slug": ("title",)}
    filter_horizontal = ('category',)
    # list_display = ('title', 'published_date', 'start_date', 'end_date', 'main_page')
    # list_editable = ['main_page', ]
    # list_filter = ['published_date', 'main_page']
    #search_fields = ['title', 'content']

admin.site.register(Item, ItemAdmin)

class CategoryAdmin(DjangoMpttAdmin):
    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Category, CategoryAdmin)
