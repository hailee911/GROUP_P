from django.urls import path,include
from . import views

app_name = "loginpage"
urlpatterns = [
    path('login/', views.login,name="login"),
    path('id/', views.id,name="id"),
    path('pw/', views.pw,name="pw"),
    path('join01/', views.join01,name="join01"),
    path('join02/', views.join02,name="join02"),
    path('join03/', views.join03,name="join03"),
    path('join04/', views.join04,name="join04"),
]
