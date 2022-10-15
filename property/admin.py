from django.contrib import admin

from .models import Complaint
from .models import Flat


class FlatAdmin(admin.ModelAdmin):
    fields = ('town',
              'address',
              'owner',
              'construction_year',
              'new_building',
              'price',
              'liked_by',
              'owners_phonenumber',
              'owners_pure_phone',      
              'created_at')
    search_fields = ('town', 'address')
    readonly_fields = ('created_at', )

    list_display = ('town',
                    'address',
                    'owner',
                    'construction_year',
                    'new_building',
                    'price',
                    'owners_phonenumber',
                    'owners_pure_phone',
                    'created_at')

    list_editable = ('new_building',)
    list_filter = ('new_building', 'has_balcony', 'rooms_number')
    raw_id_fields = ('liked_by',)
admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    fields = ('user', 'flat', 'text')
    raw_id_fields = ('user', 'flat')
admin.site.register(Complaint, ComplaintAdmin)
