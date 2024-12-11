from django.shortcuts import render
from diary.models import Letter
from loginpage.models import Member
from django.utils import timezone

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

#다이어리 작성
def diaryWrite(request):
  if request.method == "GET":
    current_date = timezone.now().date().strftime('%Y-%m-%d')
    return render(request,'diaryWrite.html', {'current_date': current_date})
  else:
    # id = request.session.get('session_id')
    # member = Member.objects.filter(id=id)
    # dtitle = request.POST.get('dtitle')
    # dcontent = request.POST.get('dcontent')
    # dfile = request.FILES.get('dfile','')
    # print("파일이름 : ", request.FILES)
    # print("파일 이름 : ", dfile)
    
    return render(request,'diaryWrite.html')