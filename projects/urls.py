from django.urls import path
from myapp.views import (
    ProductListCreateView, ProductDetailView,
    FeatureProductListView, FeatureProductDetailView,  # Updated import here
    BestSellingProductListView, best_selling_products, best_selling_product_detail,
    FlashSaleListView, flash_sales_list, flash_sale_detail,
    CouponListCreateView, CouponDetailView,
    OrderListCreateView, OrderDetailView
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    
    path('feature-products/', FeatureProductListView.as_view(), name='feature-product-list'),
    path('feature-products/<int:pk>/', FeatureProductDetailView.as_view(), name='feature-product-detail'),  # Updated here
    
    path('best-selling-products/', best_selling_products, name='best-selling-product-list'),
    path('best-selling-products/<int:pk>/', best_selling_product_detail, name='best-selling-product-detail'),
    
    path('flash-sales/', flash_sales_list, name='flash-sale-list'),
    path('flash-sales/<int:pk>/', flash_sale_detail, name='flash-sale-detail'),
    
    path('coupons/', CouponListCreateView.as_view(), name='coupon-list-create'),
    path('coupons/<int:pk>/', CouponDetailView.as_view(), name='coupon-detail'),
    
    path('orders/', OrderListCreateView.as_view(), name='order-list-create'),
    path('orders/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
]
