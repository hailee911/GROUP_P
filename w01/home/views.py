from django.shortcuts import render
from loginpage.models import Member


# 랜딩페이지
def landing(request):
  return render(request,'landing.html')

def main(request,user_id):
  context = {'user_id': user_id} 
  return render(request, 'main.html',context)

