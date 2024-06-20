from multiprocessing import AuthenticationError
from rest_framework import serializers
from .models import Product, FeatureProduct, BestSellingProduct, FlashSale, Coupon, Code
from .models import Code
from rest_framework import serializers
from django.conf import settings
from .models import FlashSale
from .models import Order
from .models import Enhance

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

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Code
        fields = '__all__'


class EnhanceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Enhance
        fields = '__all__'
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError("Unable to log in with provided credentials.")
        else:
            raise serializers.ValidationError("Must include 'username' and 'password'.")
