from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date')

    list_filter = ['published_date']
    search_fields = ['title', 'text']

admin.site.register(News, NewsAdmin)
