from django.urls import path,include
from . import views

app_name = "calendar1"
urlpatterns = [
    path('cal/', views.cal,name="cal"),
]
