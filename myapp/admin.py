# myapp/admin.py - Remove model registrations

from django.contrib import admin
from .models import Product, FeatureProduct, BestSellingProduct, FlashSale, Coupon , Code


admin.site.register(Product)
admin.site.register(FeatureProduct)
admin.site.register(BestSellingProduct)
admin.site.register(FlashSale)
admin.site.register(Coupon)

admin.site.register(Code)

from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number', 'total_cost', 'created_at')
    list_filter = ('created_at', 'payment_method')
    search_fields = ('first_name', 'last_name', 'email')
    readonly_fields = ('products',)