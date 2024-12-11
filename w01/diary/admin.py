from django.contrib import admin
from diary.models import DiaryBoard

@admin.register(DiaryBoard)
class DiaryBoardAdmin(admin.ModelAdmin):
  list_display = ['dno','dtitle','ddate']
  

# 우체통
from diary.models import Letter

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ['lno','member','ltitle','lcontent','ldate']