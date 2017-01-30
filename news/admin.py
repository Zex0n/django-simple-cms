from django.contrib import admin
from .models import News


class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_date', 'main_page')
    list_editable = ['main_page', ]
    list_filter = ['published_date', 'main_page']
    search_fields = ['title', 'text']

    class Media:
        js = [
            '//cdn.tinymce.com/4/tinymce.min.js',
            '/static/grappelli/tinymce_setup/tinymce4_setup.js',
        ]

admin.site.register(News, NewsAdmin)
