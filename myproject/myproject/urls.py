from django.contrib import admin
from django.urls import include, path  # Import include
from myapp.views import (ProductListCreateAPIView,
                         ProductRetrieveUpdateDestroyAPIView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productapi/', ProductListCreateAPIView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyAPIView.as_view(), name='product-detail'),


]

    # path('myapp/', include('myapp.urls')),  # Include URLs for your app
