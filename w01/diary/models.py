from django.db import models
from loginpage.models import Member

class DiaryBoard(models.Model):
  dno = models.AutoField(primary_key=True)  # 게시글 번호
  diarytit = models.CharField(max_length=1000,null=True)  # 다이어리 제목
  member = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=True)
  ## Board객체 : 좋아요 체크 - dno,member
  like_members = models.ManyToManyField(Member,default='', related_name='diary_like_member')
  dtitle = models.CharField(max_length=1000)  # 게시글 제목
  dcontent = models.TextField()  # 게시글 내용
  dhit = models.IntegerField(default=0)  # 조회수
  ddate = models.DateTimeField(auto_now=True)  # 게시글 날짜
  dlock = models.IntegerField(default=0)  # 게시글 나만보기
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