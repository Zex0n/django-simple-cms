from django.contrib import admin
from .models import Dealers, Regions


class DealersAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'show', 'file')
    list_editable = ['show']
    list_filter = ['show', 'region']
    search_fields = ['title', 'text', 'address']

    class Media:
        js = [
            # '//cdn.tinymce.com/4/tinymce.min.js',
            # '/static/grappelli/tinymce_setup/tinymce4_setup.js',
        ]

admin.site.register(Dealers, DealersAdmin)
admin.site.register(Regions)
