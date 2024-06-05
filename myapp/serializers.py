# myapp/serializers.py
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


        
# myapp/serializers.pyfrom rest_framework import serializersfrom .models import FeatureProduct
# myapp/serializers.py
from rest_framework import serializers
from .models import FeatureProduct

class FeatureProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeatureProduct
        fields = '__all__'

