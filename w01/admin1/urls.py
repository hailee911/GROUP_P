from django.urls import path,include
from . import views

app_name = "admin1"
urlpatterns = [
	# 어드민 로그인
    path('login/', views.admin_login, name="admin_login"),
	# 어드민 유저리스트
    path('admin_memList/', views.admin_memList, name="admin_memList"),
]
