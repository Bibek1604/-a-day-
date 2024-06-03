from django.contrib import admin

# Register your models here.
# coupon/admin.py
from django.contrib import admin
from .models import Coupon, Category

admin.site.register(Coupon)
admin.site.register(Category)
