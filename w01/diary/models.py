from django.db import models
from loginpage.models import Member

    
# 개인 다이어리 테이블
class MdiaryBoard(models.Model):
  mno = models.AutoField(primary_key=True)
  id = models.ForeignKey(Member,on_delete=models.DO_NOTHING, null=True)
  mtitle = models.CharField(max_length=1000)
  mdate = models.DateField(null=True)

  def __str__(self):
    return f"{self.mno},{self.id.id},{self.id.nicName},{self.mtitle},{self.mdate}"
  

  
  
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