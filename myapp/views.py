from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from .models import Product, FeatureProduct, BestSellingProduct, FlashSale, Coupon, Order
from .serializers import ProductSerializer, FeatureProductSerializer, CouponSerializer, OrderSerializer
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

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

class FeatureProductListView(generics.ListCreateAPIView):
    queryset = FeatureProduct.objects.all()
    serializer_class = FeatureProductSerializer

@api_view(['GET'])
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

def best_selling_products(request):
    products = BestSellingProduct.objects.filter(available=True)
    return render(request, 'best_selling_products.html', {'products': products})

def best_selling_product_detail(request, pk):
    product = get_object_or_404(BestSellingProduct, pk=pk)
    return render(request, 'best_selling_product_detail.html', {'product': product})

def flash_sales_list(request):
    flash_sales = FlashSale.objects.all()
    return render(request, 'flash_sales_list.html', {'flash_sales': flash_sales})

def flash_sale_detail(request, pk):
    flash_sale = get_object_or_404(FlashSale, pk=pk)
    return render(request, 'flash_sale_detail.html', {'flash_sale': flash_sale})

@api_view(['POST'])
def apply_coupon(request):
    code = request.data.get('code')
    product_cost = request.data.get('product_cost')
    
    if not code or not product_cost:
        return Response({'error': 'Coupon code and product cost are required'}, status=status.HTTP_400_BAD_REQUEST)
    
    try:
        coupon = Coupon.objects.get(code=code)
        if coupon.is_valid():
            if product_cost < coupon.discount_amount:
                return Response({'error': 'Product cost is smaller than the discount amount'}, status=status.HTTP_400_BAD_REQUEST)
            discounted_price = product_cost - coupon.discount_amount
            return Response({'message': 'Coupon applied!', 'discounted_price': discounted_price}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'This coupon is not valid at this time'}, status=status.HTTP_400_BAD_REQUEST)
    except Coupon.DoesNotExist:
        return Response({'error': 'Invalid coupon code'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from django.shortcuts import render
from django.http import JsonResponse
from .models import Product

def search_products(request):
    query = request.GET.get('q', '')
    category = request.GET.get('category', '')
    
    products = Product.objects.all()
    
    if query:
        products = products.filter(title__icontains=query)
    
    if category:
        products = products.filter(category=category)
    
    product_list = list(products.values())
    return JsonResponse(product_list, safe=False)
