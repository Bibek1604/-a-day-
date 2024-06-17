from rest_framework import serializers
from .models import Product, FeatureProduct, BestSellingProduct, FlashSale, Coupon, Code
from .models import Code
from rest_framework import serializers
from django.conf import settings
from .models import FlashSale

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
        # fields = '__all__'

        fields = [
            'id',
            'title', 
            'description', 
            'initial_rate', 
            'final_rate', 
            'pic', 
            'discount_percent', 
            'warranty', 
            'storage', 
            'discount_percentage'  
        ]

    def get_discount_percentage(self, obj):
        if obj.initial_rate > 0:
            return ((obj.initial_rate - obj.final_rate) / obj.initial_rate) * 100
        return 0
class CouponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Coupon
        fields = '__all__'


from .models import Code

class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'

    def get_photo(self, obj):
        request = self.context.get('request')
        if obj.pic and hasattr(obj.pic, 'url'):
            photo_url = obj.pic.url
            return request.build_absolute_uri(photo_url) if request else settings.MEDIA_URL + photo_url
        return None
    

from myapp.models import Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'