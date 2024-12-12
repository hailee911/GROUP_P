from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin1/', include('admin1.urls')),
    path('loginpage/', include('loginpage.urls')),
    path('customer/', include('customer.urls')),
    path('emotion/', include('emotion.urls')),
    path('', include('home.urls')),
    path('diary/', include('diary.urls')),
    path('mypage/', include('mypage.urls')),
    path('comment/', include('comment.urls')),
    path('calendar1/', include('calendar1.urls')),
    path('family1/', include('family1.urls')),
]
