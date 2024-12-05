from django.shortcuts import render

# 회원가입페이지
def join01(request):
  return render(request,'join01.html')


# 비밀번호찾기1
def pw(request):
  return render(request,'pw.html')


# 아이디찾기1
def id(request):
  return render(request,'id.html')


# 로그인페이지
def login(request):
  return render(request,'login.html')