from django.urls import path,include
from . import views

app_name = "admin1"
urlpatterns = [
	# 관리자1 로그인
    path('login/', views.admin_login, name="admin_login"),
	# 관리자1 - 관리자리스트
    path('admin_adminList/', views.admin_adminList, name="admin_adminList"),
	# 관리자1 - 회원관리(유저리스트)
    path('admin_memList/', views.admin_memList, name="admin_memList"),
	# 관리자1 - 회원추가
    path('admin_memAdd/', views.admin_memAdd, name="admin_memAdd"),
	# 관리자1 - 포스트
    path('admin_postList/', views.admin_postList, name="admin_postList"),
	# 관리자1 - 공지사항 
    path('admin_noticeList/', views.admin_noticeList, name="admin_noticeList"),
	# 관리자1 - 공지사항 글쓰기
    path('admin_notiWrite/', views.admin_notiWrite, name="admin_notiWrite"),
]
