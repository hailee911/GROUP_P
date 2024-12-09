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
	# 관리자추가
    path('admin_adminAdd/', views.admin_adminAdd, name="admin_adminAdd"),
	# 공지사항리스트
    path('admin_noticeList/', views.admin_noticeList, name="admin_noticeList"),
	# 공지사항쓰기
    path('admin_notiWrite/', views.admin_notiWrite, name="admin_notiWrite"),
	# 포스트리스트
    path('admin_postList/', views.admin_postList, name="admin_postList"),
	# 유저상세정보페이지
    path('admin_memView/<str:id>/', views.admin_memView, name="admin_memView"),
	# 유저정보수정페이지
    path('admin_memUpdate/<str:id>/', views.admin_memUpdate, name="admin_memUpdate"),
	# 유저삭제
    path('admin_memDelete/<str:id>/', views.admin_memDelete, name="admin_memDelete"),
	# 유저삭제(여러명 동시 삭제)
    path('admin_memsDelete/', views.admin_memsDelete, name="admin_memsDelete"),
	# 유저추가페이지
    path('admin_memAdd/', views.admin_memAdd, name="admin_memAdd"),


]
