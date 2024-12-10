from django.shortcuts import render

# 캘린더
def cal(request):
  return render(request,'calendar.html')
