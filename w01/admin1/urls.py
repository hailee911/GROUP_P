from django.urls import path,include
from . import views

app_name = "admin1"
urlpatterns = [
	# 관리자1 로그인
    path('login/', views.admin_login, name="admin_login"),
	# 어드민 로그아웃
    path('logout/', views.admin_logout, name="admin_logout"),
	# 유저리스트
    path('admin_memList/', views.admin_memList, name="admin_memList"),
	# 관리자리스트
    path('admin_adminList/', views.admin_adminList, name="admin_adminList"),
]
