from  rest_framework import serializers 
from  myapp.models import Category , Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name', 'category_id']
        
class ProductSerializer(serializers.ModelSerializer):  ###blueprint of an object
    class Meta:
        model = Product
        fields= [ 'category','name','picture','description','price_in_npr']