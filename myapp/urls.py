# myapp/urls.py
from django.urls import path
from .views import ProductListCreateView, ProductDetailView, ProductPurchaseView
from .views import FeatureProductListView, feature_product_detail_view


urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('buy/<int:pk>/', ProductPurchaseView.as_view(), name='product-purchase'),
    path('feature-products/', FeatureProductListView.as_view(), name='feature-product-list'),
    path('feature-products/<int:pk>/', feature_product_detail_view, name='feature-product-detail'),
]
