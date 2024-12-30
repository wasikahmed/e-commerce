from django.contrib import admin

from .models import Customer, Staff

# Register your models here.
admin.site.register(Customer)
admin.site.register(Staff)