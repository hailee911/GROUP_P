from django.shortcuts import render


# 랜딩페이지
def landing(request):
  return render(request,'landing.html')