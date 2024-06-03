from django.shortcuts import render

# Create your views here.
# coupon/views.py
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Coupon, Category
from .serializers import CouponSerializer, UseCouponSerializer, CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer

    @action(detail=False, methods=['post'])
    def use_coupon(self, request):
        serializer = UseCouponSerializer(data=request.data)
        if serializer.is_valid():
            try:
                coupon = Coupon.objects.get(code=serializer.validated_data['code'])
                original_price = serializer.validated_data['original_price']

                if coupon.discount_amount > original_price:
                    return Response({'status': 'discount amount exceeds product price'}, status=status.HTTP_400_BAD_REQUEST)

                if coupon.is_valid():
                    if coupon.use_coupon():
                        discounted_price = original_price - coupon.discount_amount
                        return Response({
                            'status': 'coupon applied',
                            'discounted_price': discounted_price,
                            'discount_amount': coupon.discount_amount
                        })
                    else:
                        return Response({'status': 'coupon usage exceeded'}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    return Response({'status': 'invalid or expired coupon'}, status=status.HTTP_400_BAD_REQUEST)
            except Coupon.DoesNotExist:
                return Response({'status': 'coupon not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
