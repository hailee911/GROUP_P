from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('loginpage/', include('loginpage.urls')),
    path('customer/', include('customer.urls')),
    path('emotion/', include('emotion.urls')),
    path('', include('home.urls')),
    path('', include('home.urls')),
]
