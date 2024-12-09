from django.shortcuts import render

def diaryHome(requset):
  return render(requset,'diaryHome.html')


## 내 다이어리 목록
def MdiaryList(request):
  
  return render(request,'MdiaryList.html')
