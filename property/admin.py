from django.contrib import admin

from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    fields = ('town',
              'address',
              'owner',
              'construction_year',
              'new_building',
              'price',
              'created_at')
    search_fields = ('town', 'address')
    readonly_fields = ('created_at', )

    list_display = ('town',
                    'address',
                    'owner',
                    'construction_year',
                    'new_building',
                    'price',
                    'created_at')

    list_editable = ('new_building',)





admin.site.register(Flat, FlatAdmin)
