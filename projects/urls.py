# productapi/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin interface
    path('products/', include('products.urls')),  # Include URLs from the products app
]
