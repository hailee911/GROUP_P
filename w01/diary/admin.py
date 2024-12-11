from django.contrib import admin
from diary.models import MdiaryBoard

@admin.register(MdiaryBoard)
class MdiaryBoardAdmin(admin.ModelAdmin):
    list_display = ['mno','id','get_nicName', 'mtitle', 'mdate']

    # 커스텀 메서드 정의
    def get_nicName(self, obj):
        return obj.id.nicName if obj.id and hasattr(obj.id, 'nicName') else None

    # list_display에서 보이는 이름 설정
    get_nicName.short_description = '닉네임'
  


# 우체통
from diary.models import Letter

@admin.register(Letter)
class LetterAdmin(admin.ModelAdmin):
    list_display = ['lno','member','ltitle','lcontent','ldate']