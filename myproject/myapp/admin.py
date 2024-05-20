from django.contrib import admin

from .models import Category, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_in_npr', 'available_product', 'offer_price', 'is_offer_valid')
    list_filter = ('category', 'available_offer_start_date', 'available_offer_end_date')
    search_fields = ('name', 'category__name')
