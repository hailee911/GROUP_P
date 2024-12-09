from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from admin1.models import Administrator
from loginpage.models import Member
from django.db.models import Max


# 어드민 로그인
def admin_login(request):
	if request.method == 'GET':
		return render(request, 'admin_login.html')
	else:
		id = request.POST.get('user_id')
		pw = request.POST.get('user_pw')

		qs = Administrator.objects.filter(id=id,pw=pw)
		if qs:
			request.session['session_id'] = id
			request.session['session_role'] = qs[0].role

			context = {'lmsg':'1'}
		else:
			context = {'lmsg':'0'}
		return render(request, 'admin_login.html', context)
	

# 어드민 로그아웃
def admin_logout(request):
	request.session.clear()
	context = {"outMsg":'1'}
	return render(request, 'admin_memList.html', context)
	

# 유저 리스트
def admin_memList(request):
	qs = Member.objects.all()
	context = {"mlist":qs}
	return render(request, 'admin_memList.html', context)

# 유저 상세정보
def admin_memView(request,id):
	qs = Member.objects.get(id=id)
	context = {"mem":qs}
	return render(request, 'admin_memView.html', context)

# 유저 정보 수정
def admin_memUpdate(request,id):
	if request.method == "GET":
		qs = Member.objects.get(id=id)
		context = {"mem":qs}
		return render(request, 'admin_memUpdate.html', context)
	else:
		id = request.POST.get('user_id')
		name = request.POST.get('user_name')
		nicName = request.POST.get('nickname')
		mail = request.POST.get('email')
		mdate = request.POST.get('sdate')

		qs = Member.objects.get(id=id)
		qs.id = id
		qs.name = name
		qs.nicName = nicName
		qs.mail = mail
		qs.mdate = mdate
		qs.save()
		return redirect('admin1:admin_memView', id)

# 유저정보 삭제
def admin_memDelete(request,id):
	Member.objects.get(id=id).delete()

	context = {'dmsg':id}
	return render(request, 'admin_memView.html', context)

# 유저추가페이지
def admin_memAdd(request):
	if request.method == 'GET':
		return render(request, 'admin_memAdd.html')
	else:
		id = request.POST.get('user_id')
		name = request.POST.get('user_name')
		nicName = request.POST.get('nickname')
		mail = request.POST.get('email')
		birthday = request.POST.get('birthday')
		gender = request.POST.get('gender')
		mdate = request.POST.get('sdate')

		qs = Member.objects.create(id=id,name = name,nicName = nicName,mail = mail,birthday = birthday,gender = gender,mdate = mdate)
	
		qs.save()

		context = {"amsg":name}
		return render(request, 'admin_memList.html', context)


# 관리자 리스트
def admin_adminList(request):
	qs = Administrator.objects.all()
	context = {"adminList":qs}
	return render(request, 'admin_adminList.html', context)

# 관리자 추가
def admin_adminAdd(request):
	if request.method == 'GET':
		return render(request, 'admin_adminAdd.html')
	else:
		id = request.POST.get('admin_id')
		pw = request.POST.get('admin_pw')
		name = request.POST.get('admin_name')
		tel = request.POST.get('tel')
		role = request.POST.get('role')
		if role == '3':
			nickname = '수퍼관리자'
		else:
			nickname = '관리자'

		qs = Administrator.objects.create(id=id,pw=pw,name=name,nickname=nickname,tel=tel,role=role)
		no = Administrator.objects.aggregate(max_ano = Max('ano'))
		qs.ano = no['max_ano']+1
		qs.save()
		
		return redirect('/admin1/admin_adminList/')




















# @csrf_exempt  # CSRF 검사를 우회하려면 추가 (보안상 적절한 검토 필요)
def admin_memsDelete(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # 요청에서 JSON 데이터 파싱
            members_to_delete = data.get('members', [])

            # 실제로 데이터베이스에서 삭제
            for member_id in members_to_delete:
                # Member는 회원 테이블 모델로 변경해야 합니다.
                Member.objects.filter(id=member_id).delete()

            return JsonResponse({'status': 'success'}, status=200)
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)




# 공지사항 리스트
def admin_noticeList(request):
	return render(request, 'admin_noticeList.html')

# 공지사항 쓰기
def admin_notiWrite(request):
	return render(request, 'admin_notiWrite.html')


# 포스트 리스트
def admin_postList(request):
	return render(request, 'admin_postList.html')