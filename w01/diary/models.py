from django.db import models
from loginpage.models import Member

class Letter(models.Model):
  lno = models.AutoField(primary_key=True)
  id = models.ForeignKey(Member, on_delete=models.DO_NOTHING)
  ltitle = models.CharField(max_length=1000)
  lcontent = models.TextField()
  ldate = models.DateTimeField(auto_now=True)
  lhit = models.IntegerField(default=0) # 편지 읽으면 1 안읽으면 0
  
  def __str__(self):
    return f"{self.lno},{self.id},{self.ltitle},{self.lcontent},{self.ldate},{self.lhit}"
  
