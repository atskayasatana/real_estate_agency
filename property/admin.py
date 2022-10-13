from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    fields = ('town', 'address', 'owner')
    search_fields = ('town', 'address')
    

admin.site.register(Flat, FlatAdmin)
