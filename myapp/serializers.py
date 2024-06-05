# myapp/serializers.py
from rest_framework import serializers
from .models import Product
from .models import FeatureProduct
from .models import BestSellingProduct
from .models import FlashSale
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


        
# myapp/serializers.pyfrom rest_framework import serializersfrom .models import FeatureProduct
# myapp/serializers.py
from rest_framework import serializers
from .models import FeatureProduct

class FeatureProductSerializer(serializers.ModelSerializer):
    discount_percent = serializers.DecimalField(max_digits=5, decimal_places=2, coerce_to_string=False)

    class Meta:
        model = FeatureProduct
        fields = '__all__'


class BestSellingProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = BestSellingProduct
        fields = '__all__'

class FlashSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = FlashSale
        fields = '__all__'