from django.contrib import admin
from diary.models import DiaryBoard

@admin.register(DiaryBoard)
class BoardAdmin(admin.ModelAdmin):
  list_display = ['dno','dtitle','ddate']