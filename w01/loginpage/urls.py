from django.urls import path,include
from . import views

app_name = "loginpage"
urlpatterns = [
    path('login/', views.login,name="login"),
    path('id/', views.id,name="id"),
    path('pw/', views.pw,name="pw"),
    path('join01/', views.join01,name="join01"),
]
