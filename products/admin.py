from django.contrib import admin
from .models import Product

# Register your models here.

# class ProductAdmin(admin.ModelAdmin):
  # list_display = ('name', 'price', 'is_available', 'expiry_date', 'desc')

# Register your models here.
# admin.site.register(Product, ProductAdmin)
admin.site.register(Product)
