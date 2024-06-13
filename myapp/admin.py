# myapp/admin.py - Remove model registrations

from django.contrib import admin
from .models import Product, FeatureProduct, BestSellingProduct, FlashSale, Coupon ,Order ,OrderItem, Code


admin.site.register(Product)
admin.site.register(FeatureProduct)
admin.site.register(BestSellingProduct)
admin.site.register(FlashSale)
admin.site.register(Coupon)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Code)