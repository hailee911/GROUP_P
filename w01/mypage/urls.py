from django.urls import path,include
from . import views

app_name = "mypage"
urlpatterns = [
    path('main/', views.main, name="main"),
    path('modify/', views.modify, name="modify"),
    path('modify/currpw_chk/', views.currpw_chk, name="currpw_chk"),
    path('modify/pw_chg/', views.pw_chg, name="pw_chg"),
]
