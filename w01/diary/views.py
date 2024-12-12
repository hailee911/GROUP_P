from django.shortcuts import render, redirect
from loginpage.models import Member
from diary.models import Letter
from loginpage.models import Member
from django.utils import timezone
from diary.models import Content
from diary.models import GroupDiary
from django.http import HttpResponse


# 우체통

def diaryHome(request):
  qs = Letter.objects.all().order_by("ldate")
  id = request.session.get('session_id')
  member = Member.objects.filter(id=id)
  if member:
    user_nic = member[0].nicName
    context = {"list":qs ,'user_nic':user_nic}
  else:
    context = {'list':qs}
    
  return render(request,'diaryHome.html', context)




## 가족다이어리 생성
def diaryMake(requset):
  return render(requset,'diaryMake.html')


## 내 다이어리 목록
# def MdiaryList(request):
#   qs = Content.objects.all().order_by("-cdate")
#   context = {'content':qs}  
#   return render(request,'MdiaryList.html', context)

from django.contrib.auth.decorators import login_required

@login_required
def MdiaryList(request):
    if request.method == "GET":
        # 세션에 저장된 ID 가져오기
        session_id = request.session.get('session_id')  # 세션에서 'session_id'를 가져옴
        print("세션아이디:", session_id)

        # 세션에 해당하는 ID가 존재하는지 확인
        if not session_id:
            return render(request, 'error.html', {'message': '세션 ID가 존재하지 않습니다.'})
        
        # session_id를 기준으로 Member 찾기
        member = Member.objects.filter(id=session_id).first()

        # member가 없으면 에러 처리
        if not member:
            return render(request, 'error.html', {'message': '사용자 정보가 존재하지 않습니다.'})

        # 해당 멤버의 Content 가져오기
        qs = Content.objects.filter(member=member).order_by("-cdate")
        context = {'content': qs}
        return render(request, 'MdiaryList.html', context)






# 다이어리 작성 저장
def diaryWrite(request):
    if request.method == "GET":
        # 세션에서 사용자 ID 가져오기
        id = request.session.get('session_id')  # 현재 사용자의 ID 가져오기
        current_date = timezone.now().date().strftime('%Y-%m-%d')

        # 생성한 그룹과 참여한 그룹 가져오기
        created_group = GroupDiary.objects.filter(member__id=id).first()
        joined_group = GroupDiary.objects.filter(members__id=id).first()

        return render(request, 'diaryWrite.html', {
            'current_date': current_date,
            'created_group': created_group,
            'joined_group': joined_group,
        })
    
    elif request.method == "POST":
        # 세션에서 사용자 ID 가져오기
        id = request.session.get('session_id')  # 세션에서 사용자 ID 가져오기
        
        if not id:
            return HttpResponse("로그인 정보가 없습니다.", status=400)

        # Member 모델에서 해당 ID로 회원 조회
        member = Member.objects.filter(id=id).first()  # 없으면 None 반환
        
        if not member:
            return HttpResponse("사용자 정보가 존재하지 않습니다.", status=400)
        
        # 다이어리 작성 내용 저장
        title = request.POST.get('title')
        content = request.POST.get('content')
        image = request.FILES.get('image')
        
        # 로그인 후 첫 접속 시 세션에 diary_count 초기화 (새로운 세션 시작)
        if f"diary_count_{id}" not in request.session:
            request.session[f"diary_count_{id}"] = 1
        else:
            # 세션에 diary_count가 있으면 증가
            diary_count = request.session[f"diary_count_{id}"] + 1
            request.session[f"diary_count_{id}"] = diary_count

        # cno는 세션 고유 번호로 관리된 카운터 값 사용
        cno = str(request.session[f"diary_count_{id}"])

        # Content 객체 생성하여 저장
        new_diary = Content(
            cno=cno, #생성된 cno사용
            member=member, 
            ctitle=title,
            ccontent=content,
            image=image,
            cdate=timezone.now().date()
        )
        new_diary.save()

        return redirect('diary:MdiaryList')  # 다이어리 리스트로 리다이렉트


# 다이어리 view
def diaryView(request):
  return render(request,'diary_view.html')