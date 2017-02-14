from django.contrib import admin
from .models import Dealers, Regions


class DealersAdmin(admin.ModelAdmin):
    list_display = ('title', 'region', 'show', 'file')
    list_editable = ['show']
    list_filter = ['show', 'region']
    search_fields = ['title', 'text', 'address']

    class Media:
        css = {
            'all': ('/static/admin/css/cmsadmin.css',)
        }

admin.site.register(Dealers, DealersAdmin)
admin.site.register(Regions)
