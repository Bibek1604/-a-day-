# coupon/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CouponViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'coupons', CouponViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
