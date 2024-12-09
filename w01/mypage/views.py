from django.shortcuts import render
from loginpage.models import Member
from django.http import JsonResponse, HttpResponse


# Create your views here.
def main(request):
  return render(request, 'mymain.html')

def modify(request):
  # 회원 정보 수정 불러오기
  id = request.session['session_id']
  qs = Member.objects.filter(id=id)
  email = qs[0].mail.split('@')
  context = {'mem_info':qs[0], 'mail_id':email[0], 'mail_domain':email[1]}
  print(email[1])
  return render(request, 'mypage_modi.html', context)

def currpw_chk(request):
  pw = request.POST.get('currPw','')
  qs = Member.objects.filter(pw=pw)
  print(qs[0])

  if qs:
    context = {'result':'success'}
  else:
    context = {'result':'fail'}

  return JsonResponse(context) 