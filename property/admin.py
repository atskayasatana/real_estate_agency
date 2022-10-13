from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    fields = ('town', 'address', 'owner', 'created_at')
    search_fields = ('town', 'address')
    readonly_fields = ('created_at', )


admin.site.register(Flat, FlatAdmin)
