from django.contrib import admin
from .models import Car, Sale, Client

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'price', 'color', 'fuel_type')
    list_filter = ('year', 'fuel_type', 'body_type')
    search_fields = ('model',)

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ('car', 'client', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'name', 'phone_number')
    search_fields = ('last_name', 'phone_number')