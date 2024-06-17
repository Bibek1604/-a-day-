from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


from django.contrib import admin
from myapp.views import (
    ProductListCreateView, ProductDetailView,
    FeatureProductListView, FeatureProductDetailView,  # Updated import here
    best_selling_products, best_selling_product_detail,
     flash_sales_list, flash_sale_detail,
    CouponListCreateView, CouponDetailView, flash_sales_list, flash_sale_detail, best_selling_products, best_selling_product_detail,
   search_view,code_view,OrderListCreateView
)


from myapp.models import Code

urlpatterns = [
    path('admin/', admin.site.urls),


    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    
    path('feature-products/', FeatureProductListView.as_view(), name='feature-product-list'),
    path('feature-products/<int:pk>/', FeatureProductDetailView.as_view(), name='feature-product-detail'),  # Updated here
    
    path('flash-sales/', flash_sales_list, name='flash-sale-list'),
    path('flash-sales/<int:pk>/', flash_sale_detail, name='flash-sale-detail'),
    path('best-selling-products/', best_selling_products, name='best-selling-product-list'),
    path('best-selling-products/<int:pk>/', best_selling_product_detail, name='best-selling-product-detail'),

    
    path('coupons/', CouponListCreateView.as_view(), name='coupon-list-create'),
    path('coupons/<int:pk>/', CouponDetailView.as_view(), name='coupon-detail'),


    path('search/', search_view, name='search'),

    path('code/', code_view, name='code'),
    path('order/', OrderListCreateView.as_view(), name='order-list-create'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

