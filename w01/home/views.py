from django.shortcuts import render, redirect
from loginpage.models import Member


# 랜딩페이지
def landing(request):
  return render(request,'landing.html')

def main(request):
  id = request.session['session_id']
  qs = Member.objects.filter(id=id)

  context = {'my':qs[0]}
  return render(request, 'main.html',context)

def logout(request):
  request.session.clear()
  return redirect('/')