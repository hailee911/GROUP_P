from django.db import models
from loginpage.models import Member

class DiaryBoard(models.Model):
  dno = models.AutoField(primary_key=True)
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=True)
  ## Board객체 : 좋아요 체크 - dno,member
  dtitle = models.CharField(max_length=1000)
  dcontent = models.TextField()
  dhit = models.IntegerField(default=0)
  ddate = models.DateTimeField(auto_now=True)
  # img 파일업로드
  dfile = models.ImageField(null=True,upload_to='diary')

  def __str__(self):
    return f"{self.dno},{self.dtitle},{self.ddate}"
  
  
# 우체통
from loginpage.models import Member
class Letter(models.Model):
  lno = models.AutoField(primary_key=True)
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=True)
  ltitle = models.CharField(max_length=1000)
  lcontent = models.TextField()
  ldate = models.DateTimeField(auto_now=True)
  lhit = models.IntegerField(default=0)

  def __str__(self):
    return f"{self.lno},{self.member},{self.ltitle},{self.lcontent},{self.ldate}"
  
  
# 그룹 다이어리 db
class GroupDiary(models.Model):
  gno = models.AutoField(primary_key=True)
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=False)
  gtitle = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f"{self.gno},{self.member.id},{self.gtitle},{self.created_at}"

# 다이어리 작성 -> 내용 db
from django.utils import timezone
class Content(models.Model):
  cno = models.AutoField(primary_key=True)
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=False) # 유저id & 닉네임 가져옴
  ctitle = models.CharField(max_length=1000)
  ccontent = models.TextField(null=True)
  cdate = models.DateField(default=timezone.now)  # 기본값을 오늘 날짜로 설정
  group_diary  = models.ForeignKey(GroupDiary, on_delete=models.CASCADE, null=True, blank=True)
  # 공용다이어리 db 만들면 추후 업데이트
  image = models.ImageField(upload_to='diary_images/', blank=True, null=True)  # 이미지

  def __str__(self):
    return f"{self.cno},{self.member.id},{self.ctitle},{self.ccontent},{self.cdate},{self.group_diary},{self.member.nicName}"