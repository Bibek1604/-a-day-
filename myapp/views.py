from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from .models import Product, FeatureProduct, BestSellingProduct, FlashSale, Coupon, Order, Code
from .serializers import (
    ProductSerializer,
    FeatureProductSerializer,
    BestSellingProductSerializer,
    FlashSaleSerializer,
    CouponSerializer,
    OrderSerializer,
    CodeSerializer
)

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductPurchaseView(APIView):
    def post(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        
        if product.stock > 0:
            product.stock -= 1
            product.save()
            return Response({'message': 'Purchase successful', 'remainingStock': product.stock}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Out of stock'}, status=status.HTTP_400_BAD_REQUEST)

class FeatureProductListView(generics.ListCreateAPIView):
    queryset = FeatureProduct.objects.all()
    serializer_class = FeatureProductSerializer

class FeatureProductDetailView(generics.RetrieveAPIView):
    queryset = FeatureProduct.objects.all()
    serializer_class = FeatureProductSerializer


@api_view(['GET'])
def flash_sales_list(request):
    flash_sales = FlashSale.objects.all()
    serializer = FlashSaleSerializer(flash_sales, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def best_selling_products(request):
    best_selling = BestSellingProduct.objects.all()
    serializer = BestSellingProductSerializer(best_selling, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def best_selling_product_detail(request, pk):
    product = get_object_or_404(BestSellingProduct, pk=pk)
    serializer = BestSellingProductSerializer(product)
    return Response(serializer.data)


@api_view(['GET'])
def flash_sale_detail(request, pk):
    flash_sale = get_object_or_404(FlashSale, pk=pk)
    serializer = FlashSaleSerializer(flash_sale)
    return Response(serializer.data)

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

class ProductsByCategoryList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        category = self.kwargs['category']
        return Product.objects.filter(category=category, available=True)

class FlashSaleListView(generics.ListAPIView):
    queryset = FlashSale.objects.all()
    serializer_class = FlashSaleSerializer

class BestSellingProductListView(generics.ListAPIView):
    queryset = BestSellingProduct.objects.all()
    serializer_class = BestSellingProductSerializer

class CouponListCreateView(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class CouponDetailView(generics.RetrieveAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetailView(generics.RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

def search_view(request):
    query = request.GET.get('q')
    search_results = Product.objects.filter(title__icontains=query) if query else None
    return render(request, 'search_results.html', {'search_results': search_results, 'query': query})

@api_view(['GET'])
def code_view(request):
    codes = Code.objects.all()
    serializer = CodeSerializer(codes, many=True)
    return Response(serializer.data)
