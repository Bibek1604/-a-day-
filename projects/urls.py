from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from myapp.views import (
    ProductListCreateView, ProductDetailView,
    FeatureProductListView, FeatureProductDetailView,
    best_selling_products, best_selling_product_detail,
    flash_sales_list, flash_sale_detail,
    CouponListCreateView, CouponDetailView,
     code_view, create_order,enhance_view,LoginView,AddToCartView,GetCartView ,NotificationView,search_titles
)

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from myapp.views import RegisterUserView
from myapp.models import Enhance
urlpatterns = [
    path('admin/', admin.site.urls),

    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    
    path('feature-products/', FeatureProductListView.as_view(), name='feature-product-list'),
    path('feature-products/<int:pk>/', FeatureProductDetailView.as_view(), name='feature-product-detail'),
    
    path('flash-sales/', flash_sales_list, name='flash-sale-list'),
    path('flash-sales/<int:pk>/', flash_sale_detail, name='flash-sale-detail'),
    
    path('best-selling-products/', best_selling_products, name='best-selling-product-list'),
    path('best-selling-products/<int:pk>/', best_selling_product_detail, name='best-selling-product-detail'),
    
    path('coupons/', CouponListCreateView.as_view(), name='coupon-list-create'),
    path('coupons/<int:pk>/', CouponDetailView.as_view(), name='coupon-detail'),
    
    path('code/', code_view, name='code'),
    path('order/', create_order, name='order-list-create'),
    path('enhance/', enhance_view, name='enhance'),

    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('add_to_cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('get_cart/', GetCartView.as_view(), name='get_cart'),

        path('search/', search_titles, name='search_titles'),
    


    path('notification/', NotificationView.as_view(), name='notification'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
