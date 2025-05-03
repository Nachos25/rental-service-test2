from django.contrib import admin
from .models import Apartment


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'price', 'number_of_rooms', 
        'square', 'availability', 'owner'
    )
    list_filter = ('availability', 'number_of_rooms')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}
