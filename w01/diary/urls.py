from django.urls import path,include
from . import views

app_name = "diary"

urlpatterns = [
    path('diaryHome/', views.diaryHome, name="diaryHome"),
    path('MdiaryList/', views.MdiaryList, name="MdiaryList"),
]
