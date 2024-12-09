from django.shortcuts import render
from diary.models import DiaryBoard
from loginpage.models import Member

def diaryHome(requset):
  return render(requset,'diaryHome.html')


## 내 다이어리 목록
def MdiaryList(request):
  qs = DiaryBoard.objects.all()
  for i in qs:
    print(i.diarytit)
    print(i.dtitle)
    print(i.dcontent)
    print('-=' * 39)
  context = {"MdiaryList":qs}
  return render(request,'MdiaryList.html',context)
