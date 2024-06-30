from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from django.shortcuts import render, get_object_or_404
from .models import Product, FeatureProduct, BestSellingProduct, FlashSale, Coupon, Code
from .serializers import (
    ProductSerializer,
    FeatureProductSerializer,
    BestSellingProductSerializer,
    FlashSaleSerializer,
    CouponSerializer,
    codeSerializer,
    OrderSerializer,
    RecommendationSerializer
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
from myapp.serializers import RecommendationSerializer
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from myapp.models import Recommendation
from myapp.serializers import RecommendationSerializer



@api_view(['GET'])
def recommendation_list_detail(request, pk):
    try:
        recommendation = Recommendation.objects.get(pk=pk)
    except Recommendation.DoesNotExist:
        return Response(status=404)
    serializer = RecommendationSerializer(recommendation)
    return Response(serializer.data)

class RecommendationListCreate(generics.ListCreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

class RecommendationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
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





@api_view(['GET'])
def code_view(request):
    codes = Code.objects.all()
    serializer = codeSerializer(codes, many=True)
    return Response(serializer.data)



from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import OrderSerializer
@api_view(['POST'])
def create_order(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Enhance
from .serializers import EnhanceSerializer

@api_view(['GET'])
def enhance_view(request):
    enhances = Enhance.objects.all()
    serializer = EnhanceSerializer(enhances, many=True)
    return Response(serializer.data)






from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer, LoginSerializer, CartItemSerializer

class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddToCartView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            cart = request.session.get('cart', [])
            cart.append(serializer.validated_data)
            request.session['cart'] = cart
            return Response({'status': 'Item added to cart'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GetCartView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cart = request.session.get('cart', [])
        return Response(cart, status=status.HTTP_200_OK)



from myapp.serializers import NotificationSerializer
from rest_framework import status
from .models import Notification  

class NotificationView(APIView):
    def get(self, request):
        notifications = Notification.objects.all()  
        notifications_data = [
            {"id": notification.id, "Title": notification.title, "Description": notification.description}
            for notification in notifications
        ]
        return Response(notifications_data, status=status.HTTP_200_OK)  
# views.py
from django.http import JsonResponse
from django.db.models import Q
from .models import Product, FeatureProduct, BestSellingProduct, FlashSale

def search_products(request):
    query = request.GET.get('q', '')
    product_results = Product.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )
    feature_product_results = FeatureProduct.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )
    best_selling_product_results = BestSellingProduct.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )
    flash_sale_results = FlashSale.objects.filter(
        Q(title__icontains=query) |
        Q(description__icontains=query)
    )

    results = {
        'products': list(product_results.values()),
        'feature_products': list(feature_product_results.values()),
        'best_selling_products': list(best_selling_product_results.values()),
        'flash_sales': list(flash_sale_results.values()),
    }

    return JsonResponse(results, safe=False)



#this much