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
    list_filter = ('new_building', 'has_balcony', 'rooms_number')


admin.site.register(Flat, FlatAdmin)
