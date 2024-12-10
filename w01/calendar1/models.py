from django.db import models
from loginpage.models import Member

class Event(models.Model):
    # 고유번호는 자동 증가하는 IntegerField
    no = models.AutoField(primary_key=True)  # AutoField는 자동으로 증가하는 고유번호
    
    # 작성자 이름은 Member 모델과 ForeignKey로 연결
    name = models.ForeignKey(Member, on_delete=models.CASCADE,null=True)  # 작성자는 다른 모델에서 가져옵니다
    
    title = models.CharField(max_length=255)  # 제목
    start_date = models.DateTimeField()  # 시작 시간
    end_date = models.DateTimeField()  # 종료 시간
    location = models.CharField(max_length=255, blank=True, null=True)  # 장소, 빈 값 허용
    
    # 반복 필드는 선택 가능한 옵션으로 설정
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
        default='none'  # 기본값은 '없음'
    )

    memo = models.TextField(blank=True, null=True)  # 메모, 빈 값 허용
    created_at = models.DateTimeField(auto_now_add=True)  # 생성일, 생성 시 자동 저장
    
    def __str__(self):
        return self.title
