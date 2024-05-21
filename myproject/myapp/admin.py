from django.contrib import admin

from .models import Cart, Category, Coupon, Product


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price_in_npr', 'available_product', 'offer_price', 'is_offer_valid')
    list_filter = ('category', 'available_offer_start_date', 'available_offer_end_date')
    search_fields = ('name', 'category__name')

@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'discount_percent', 'valid_from', 'valid_to')
    list_filter = ('valid_from', 'valid_to')
    search_fields = ('code',)

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'product', 'price', 'battery_health_condition', 'coupon_code')
    list_filter = ('category', 'coupon_code')
    search_fields = ('user__username', 'product__name', 'coupon_code__code')
