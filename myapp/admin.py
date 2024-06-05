from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, FeatureProduct

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'initial_rate', 'final_rate', 'color', 'available', 'stock')

class FeatureProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'initial_price', 'final_price', 'sale_end_time', 'Category')

admin.site.register(Product, ProductAdmin)
admin.site.register(FeatureProduct, FeatureProductAdmin)
