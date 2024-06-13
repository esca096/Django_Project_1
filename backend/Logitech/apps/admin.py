from django.contrib import admin
from .models import Product
# Register your models here.

class AdminAppsProduct(admin.ModelAdmin):
    list_display = ('name', 'content', 'price')


admin.site.register(Product, AdminAppsProduct)