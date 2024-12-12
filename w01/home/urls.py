from django.urls import path,include
from . import views

app_name = "main"
urlpatterns = [
    path('', views.landing,name="landing"),
    path('index/<str:user_id>', views.main,name="main"),
]
