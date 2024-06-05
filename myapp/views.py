# myapp/views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import FeatureProduct
from .serializers import FeatureProductSerializer
from django.utils import timezone

from .serializers import ProductSerializer

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductPurchaseView(APIView):
    def post(self, request, pk):
        try:
            product = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        if product.stock > 0:
            product.stock -= 1
            product.save()
            return Response({'message': 'Purchase successful', 'remainingStock': product.stock}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Out of stock'}, status=status.HTTP_400_BAD_REQUEST)

# myapp/views.py

# myapp/views.py
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import FeatureProduct
from .serializers import FeatureProductSerializer
from django.utils import timezone

class FeatureProductListView(generics.ListCreateAPIView):
    queryset = FeatureProduct.objects.all()
    serializer_class = FeatureProductSerializer

def feature_product_detail_view(request, pk):
    feature_product = get_object_or_404(FeatureProduct, pk=pk)
    sale_end_time = feature_product.sale_end_time
    current_time = timezone.now()
    time_remaining = sale_end_time - current_time

    context = {
        'feature_product': feature_product,
        'time_remaining': time_remaining,
    }

    return render(request, 'feature_product_detail.html', context)

