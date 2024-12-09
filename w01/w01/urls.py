from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin1/', include('admin1.urls')),
    path('loginpage/', include('loginpage.urls')),
    path('customer/', include('customer.urls')),
    path('emotion/', include('emotion.urls')),
    path('', include('home.urls')),
    path('main/', include('home.urls')),
    path('diary/', include('diary.urls')),
]
