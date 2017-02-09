from django.contrib import admin
from .models import Promotions


class PromotionsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'start_date', 'end_date', 'main_page')
    list_editable = ['main_page', ]
    list_filter = ['published_date', 'main_page']
    search_fields = ['title', 'text']

admin.site.register(Promotions, PromotionsAdmin)
