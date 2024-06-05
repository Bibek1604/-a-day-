from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product, FeatureProduct
from .models import BestSellingProduct
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'initial_rate', 'description','final_rate', 'color', 'available', 'stock')

class FeatureProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'initial_price', 'final_price', 'discount_percent', 'category' ,'description')  # Assuming 'category' is a valid attribute of FeatureProduct

class BestSellingProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'initial_rate', 'description','final_rate', 'color', 'available', 'stock')

admin.site.register(Product)
admin.site.register(FeatureProduct)
admin.site.register(BestSellingProduct)