from rest_framework import serializers
from .models import Product, FeatureProduct, BestSellingProduct, FlashSale, Coupon, Order

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class FeatureProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureProduct
        fields = '__all__'

class BestSellingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSellingProduct
        fields = '__all__'

class FlashSaleSerializer(serializers.ModelSerializer):
    discount_percentage = serializers.SerializerMethodField()

    class Meta:
        model = FlashSale
        fields = '__all__'

    def get_discount_percentage(self, obj):
        if obj.initial_price > 0:
            return ((obj.initial_price - obj.final_price) / obj.initial_price) * 100
        return 0
from .models import Coupon

class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
