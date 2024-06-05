# myapp/urls.py
from django.urls import path
from .views import ProductListCreateView, ProductDetailView, ProductPurchaseView

urlpatterns = [
    path('', ProductListCreateView.as_view(), name='product-list-create'),
    path('<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('buy/<int:pk>/', ProductPurchaseView.as_view(), name='product-purchase'),
]
