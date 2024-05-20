from django.contrib import admin
from django.urls import include, path  # Import include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('myapp/', include('myapp.urls')),  # Include URLs for your app
]
