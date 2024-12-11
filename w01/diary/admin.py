from django.contrib import admin
from diary.models import DiaryBoard

@admin.register(DiaryBoard)
class BoardAdmin(admin.ModelAdmin):
  list_display = ['dno','dtitle','ddate']
  

# 우체통
from diary.models import Letter

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ['lno','member','ltitle','lcontent','ldate']
    

# 그룹다이어리 & 내용
from diary.models import GroupDiary,Content    
@admin.register(GroupDiary)
class GroupDiaryAdmin(admin.ModelAdmin):
    list_display = ['gno','member_id','gtitle','created_at']
    
from django.contrib import admin
from .models import Content

@admin.register(Content)
class ContentAdmin(admin.ModelAdmin):
    list_display = ['cno', 'member_id', 'ctitle', 'ccontent', 'cdate', 'group_diary', 'member_nicName']

    # member_nicName을 반환하는 메서드 정의
    def member_nicName(self, obj):
        return obj.member.nicName if obj.member else None
    
    # member_nicName으로 정렬 가능하게 설정
    member_nicName.admin_order_field = 'member__nicName'
    
    # 컬럼 제목 설정
    member_nicName.short_description = 'Member Nickname'
