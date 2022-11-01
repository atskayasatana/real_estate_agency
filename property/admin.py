from django.contrib import admin

from .models import Complaint
from .models import Flat
from .models import Owner

class OwnerInstanceInline(admin.TabularInline):
    model=Flat.flat_owner.through
    raw_id_fields = ('flat','owner')
    fields = ('owner',)
    list_display =('owner')

class FlatAdmin(admin.ModelAdmin):
    fields = ('town',
              'address',
              'construction_year',
              'new_building',
              'price',
              'liked_by',
              'created_at')
    search_fields = ('town', 'address')
    readonly_fields = ('created_at', )

    list_display = ('town',
                    'address',
                    'construction_year',
                    'new_building',
                    'price',
                    'created_at')

    list_editable = ('new_building',)
    list_filter = ('new_building', 'has_balcony', 'rooms_number')
    raw_id_fields = ('liked_by',)
    inlines = (OwnerInstanceInline,)
admin.site.register(Flat, FlatAdmin)


class ComplaintAdmin(admin.ModelAdmin):
    fields = ('user', 'flat', 'text')
    raw_id_fields = ('user', 'flat')
admin.site.register(Complaint, ComplaintAdmin)

class OwnerAdmin(admin.ModelAdmin):
    fields = ('owner', 'owners_phonenumber', 'owners_pure_phone', 'flat')
    list_display = ('owner', 'owners_phonenumber', 'owners_pure_phone')
    raw_id_fields = ('flat',)
admin.site.register(Owner, OwnerAdmin)
