from django.contrib import admin
from .models import Customer

class CustomerAdmin(admin.ModelAdmin):
  list_display = ('first_name', 'last_name', 'email', 'contact', 'desc')

# Register your models here.
admin.site.register(Customer, CustomerAdmin)
