# myapp/admin.py - Remove model registrations

from django.contrib import admin
from .models import Product, FeatureProduct, BestSellingProduct, FlashSale, Coupon

admin.site.register(Product)
admin.site.register(FeatureProduct)
admin.site.register(BestSellingProduct)
admin.site.register(FlashSale)
admin.site.register(Coupon)
