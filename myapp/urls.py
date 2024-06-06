# myapp/urls.py
from django.urls import path
from .views import (
    ProductListCreateView, ProductDetailView, ProductPurchaseView,
    FeatureProductListView, feature_product_detail_view, 
    flash_sale_detail, best_selling_products, 
    best_selling_product_detail, flash_sales_list, flash_sale_detail
    
)
from .views import apply_coupon

from myapp import   views


urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('buy/<int:pk>/', ProductPurchaseView.as_view(), name='product-purchase'),
    path('feature-products/', FeatureProductListView.as_view(), name='feature-product-list'),
    path('feature-products/<int:pk>/', feature_product_detail_view, name='feature-product-detail'),
    path('best-selling-products/', views.best_selling_products, name='best_selling_products'),
    path('best-selling-products/<int:pk>/', views.best_selling_product_detail, name='best_selling_product_detail'),
    path('flash-sales/', flash_sales_list, name='flash_sales'),
    path('flash-sales/<int:pk>/', flash_sale_detail, name='flash_sale_detail'),
    path('api/apply-coupon/', apply_coupon, name='apply_coupon'),

]

