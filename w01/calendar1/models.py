from django.db import models
from django.core.exceptions import ValidationError
from django.utils.timezone import now
from loginpage.models import Member

class Event(models.Model):
    # 고유번호는 자동 증가하는 IntegerField
    no = models.AutoField(primary_key=True)
    
    # 작성자 이름은 Member 모델과 ForeignKey로 연결
    name = models.ForeignKey(Member, on_delete=models.CASCADE, null=True, blank=True)
    
    title = models.CharField(max_length=255, default="제목이없습니다.")
    start_date = models.DateTimeField(default=now)  # 시작 시간
    end_date = models.DateTimeField()  # 종료 시간
    location = models.CharField(max_length=255, blank=True, null=True)
    
    REPEAT_CHOICES = [
        ('none', '없음'),
        ('daily', '매일'),
        ('weekly', '매주'),
        ('monthly', '매월'),
        ('yearly', '매년'),
    ]
    repeat = models.CharField(
        max_length=10,
        choices=REPEAT_CHOICES,
        default='none'
    )
    
    memo = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def clean(self):
        if self.start_date and self.end_date and self.end_date <= self.start_date:
            raise ValidationError('종료 시간은 시작 시간 이후여야 합니다.')
    
    def __str__(self):
        return f"{self.title} ({self.start_date.strftime('%Y-%m-%d')})"
