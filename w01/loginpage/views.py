from django.shortcuts import render,redirect
from loginpage.models import Member
from django.contrib import messages



import smtplib
import random
import string
from email.mime.text import MIMEText
from django.shortcuts import render
from django.http import HttpResponse

# 전역 변수로 인증 코드와 이메일을 저장
verification_code = None
user_email = None

def generate_verification_code():
  """랜덤 인증 코드를 생성하는 함수"""
  return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

def send_verification_email(email, code):
  """이메일로 인증 코드를 보내는 함수"""
  smtpName = "smtp.naver.com"
  smtpPort = 587
  sendEmail = "wonwow55@naver.com"
  pw = "j951852753"  # 비밀번호는 실제로 안전한 방법으로 관리해야 합니다.
  title = "이메일 인증 코드"
  content = f"인증 코드: {code}"

  msg = MIMEText(content)
  msg['Subject'] = title
  msg['From'] = sendEmail
  msg['To'] = email

  try:
    s = smtplib.SMTP(smtpName, smtpPort)
    s.starttls()  # TLS 연결 설정
    s.login(sendEmail, pw)  # 로그인
    s.sendmail(sendEmail, email, msg.as_string())  # 이메일 보내기
    s.quit()  # 세션 종료
    print("메일을 발송했습니다.")
  except Exception as e:
    print("메일 발송 중 오류 발생: ", e)





def id(request):
    global verification_code, user_email

    if request.method == 'POST':
        if 'email' in request.POST:
            # 이메일 입력 후 인증 코드 발송
            em1 = request.POST.get('email')  # 이메일 첫 번째 부분
            em2 = request.POST.get('em2')  # 이메일 두 번째 부분
            full_mail = f"{em1}@{em2}"  # 전체 이메일 
            user_email = full_mail
            verification_code = generate_verification_code()

            send_verification_email(user_email, verification_code)
            
            return render(request, 'id.html')

        elif 'verification_code' in request.POST:
            # 인증 코드 확인
            entered_code = request.POST['verification_code']
            if entered_code == verification_code:
                return HttpResponse("인증 성공!")
            else:
                return HttpResponse("잘못된 인증 코드입니다.")

    return render(request, 'id.html')




# 회원가입페이지4
def test(request):
  return render(request,'test.html')







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
    id = request.POST.get('id')
    if Member.objects.filter(id=id).exists():
      messages.error(request, '이미 존재하는 아이디입니다. 다른 아이디를 입력하세요.')
      return render(request,'join02.html')
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

# 비밀번호찾기3
def pw3(request):
  return render(request,'pw3.html')

# 비밀번호찾기2
def pw2(request):
  return render(request,'pw2.html')

# 비밀번호찾기1
def pw(request):
  return render(request,'pw.html')

# 아이디찾기2
def id2(request):
  return render(request,'id2.html')

# # 아이디찾기1
# def id(request):
#   return render(request,'id.html')

# 로그인페이지
def login(request):
  if request.method == "GET":
    print('확인2')
    return render(request,'login.html')
  else:
    id = request.POST.get('id')
    pw = request.POST.get('pw')
    qs = Member.objects.filter(id=id,pw=pw)
    print("확인용 :",id)

    if qs:
      request.session['session_id'] = id
      print("확인일")
      context = {"lmsg":"1"}
      return render(request,'main.html',context)
    else:
      context = {'lmsg':"0"}
      print("확인2")
      return render(request,'login.html',context)