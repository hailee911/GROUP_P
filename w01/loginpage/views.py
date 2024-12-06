from django.shortcuts import render,redirect
from .models import Member


# 회원가입페이지4
def join04(request):
  return render(request,'join04.html')

# 회원가입페이지3
def join03(request,id,pw,mail):
  if request.method == "POST":
    # `context`에서 전달된 데이터 가져오기
    id = request.POST.get('id')
    pw = request.POST.get('pw')  # 비밀번호는 암호화 필요
    mail = request.POST.get('full_mail')
    qs = Member.objects.create(
      id=id,
      pw=pw,  # 암호화 필요
      mail=mail,
      name=request.POST.get('name'),
      birthday=request.POST.get('date'),
      gender=request.POST.get('gender'),
    )
    print("정보2 : ",qs)
    return redirect('loginpage:join04')  # 성공 페이지로 이동
  else:
    print('join03 확인 : ',id,pw,mail)
    context = {       
      'id': id,
      'pw': pw,
      'full_mail' : mail
    }
    return render(request,'join03.html',context)

# 회원가입페이지2
def join02(request):
  if request.method == "POST":
    # 이메일 결합
    em1 = request.POST.get('em1')  # 이메일 첫 번째 부분
    em2 = request.POST.get('em2')  # 이메일 두 번째 부분
    full_mail = f"{em1}@{em2}"  # 전체 이메일
    print("정보1",request.POST.get('id'),request.POST.get('pw'),full_mail)
    # return render(request,'join03.html',context)  # Step 2로 이동
    return redirect('loginpage:join03',request.POST.get('id'),request.POST.get('pw'),full_mail)  # Step 2로 이동
  else:
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

# 회원가입페이지1
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