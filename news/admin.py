from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'main_page')
    list_editable = ['main_page', ]
    list_filter = ['published_date', 'main_page']
    search_fields = ['title', 'text']

admin.site.register(News, NewsAdmin)
