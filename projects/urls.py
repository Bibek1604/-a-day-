# projects/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import FeatureProductListView, feature_product_detail_view
urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin interface
    path('products/', include('myapp.urls')),  # Include URLs from the myapp
    path('Featureproducts/', include('myapp.urls')),
    path('BestSellingProducts/', include('myapp.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)