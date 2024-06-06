# projects/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from myapp.views import FeatureProductListView, feature_product_detail_view
from myapp.views import create_order


urlpatterns = [
    path('admin/', admin.site.urls),  # URL for the admin interface
    path('products/', include('myapp.urls')),  # Include URLs from the myapp
    path('Featureproducts/', include('myapp.urls')),
    path('BestSellingProducts/', include('myapp.urls')),
    path('coupencode/', include('myapp.urls')), 
    path('api/create-order/', create_order, name='create_order'),  # Named URL pattern

    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)