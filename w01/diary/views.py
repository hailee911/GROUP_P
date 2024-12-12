from django.shortcuts import render,redirect
from loginpage.models import Member
from diary.models import Letter
from loginpage.models import Member
from .models import MdiaryBoard

## 다이어리 HOME
def diaryHome(request):
  qs = Letter.objects.all().order_by("ldate")
  id = request.session.get('session_id')
  member = Member.objects.filter(id=id)
  # personal_diaries = MdiaryBoard.objects.select_related('id').all() # 개인 다이어리 데이터 가져오기
  if member:
    user_nic = member[0].nicName
    context = {"list":qs ,'user_nic':user_nic}
  else:
    context = {'list':qs}
    
  return render(request,'diaryHome.html',context)



## 가족다이어리 생성
def diaryMake(requset):
  return render(requset,'diaryMake.html')


## 내 다이어리 목록
def MdiaryList(request):
  return render(request,'MdiaryList.html')