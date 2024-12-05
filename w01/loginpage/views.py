from django.shortcuts import render

# 회원가입페이지4
def join04(request):
  return render(request,'join04.html')

# 회원가입페이지3
def join03(request):
  return render(request,'join03.html')

# 회원가입페이지2
def join02(request):
  return render(request,'join02.html')

# 회원가입페이지1-4
def join01_4(request):
  return render(request,'join01_4.html')

# 회원가입페이지1-3
def join01_3(request):
  return render(request,'join01_3.html')

# 회원가입페이지1-2
def join01_2(request):
  return render(request,'join01_2.html')

# 회원가입페이지1-1
def join01_1(request):
  return render(request,'join01_1.html')

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