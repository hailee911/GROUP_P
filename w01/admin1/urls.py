from django.urls import path,include
from . import views

app_name = "admin1"
urlpatterns = [
    path('admin1/', views.admin_login, name="admin_login"),
]
