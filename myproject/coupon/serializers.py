# coupon/serializers.py
from rest_framework import serializers
from .models import Coupon, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class UseCouponSerializer(serializers.Serializer):
    code = serializers.CharField(max_length=50)
    original_price = serializers.DecimalField(max_digits=10, decimal_places=2)
