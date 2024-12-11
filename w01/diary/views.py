from django.shortcuts import render
from diary.models import Letter
from loginpage.models import Member

def diaryHome(request):
  qs = Letter.objects.all().order_by("ldate")
  id = request.session.get('session_id')
  member = Member.objects.filter(id=id)
  if member:
    user_nic = member[0].nicName
    context = {"list":qs ,'user_nic':user_nic}
  else:
    context = {'list':qs}
    
  return render(request,'diaryHome.html', context)


## 내 다이어리 목록
def MdiaryList(request):
  
  return render(request,'MdiaryList.html')
