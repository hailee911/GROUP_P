from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from loginpage.models import Member
from django.db.models import Max
from admin1.models import Administrator
from customer.models import NoticeBoard


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

# 체크박스 유저 삭제
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

# 관리자 상세보기
def admin_adminView(request,id):
	qs = Administrator.objects.get(id=id)
	context = {"admin":qs}
	return render(request, 'admin_adminView.html', context)

# 관리자 정보수정
def admin_adminUpdate(request,id):
	if request.method == 'GET':
		qs = Administrator.objects.get(id=id)
		context = {"admin":qs}
		return render(request, 'admin_adminUpdate.html', context)
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

		qs = Administrator.objects.get(id=id)
		qs.id = id
		qs.pw = pw
		qs.name = name
		qs.tel = tel
		qs.role = role
		qs.nickname = nickname
		qs.save()
		return redirect('admin1:admin_adminView', id)
	
# 관리자 삭제
def admin_adminDelete(request,id):
	Administrator.objects.get(id=id).delete()

	context = {'dmsg':id}
	return render(request, 'admin_adminView.html', context)


# 체크박스 관리자 삭제
def admin_adminsDelete(request):
	if request.method == 'POST':
			try:
					data = json.loads(request.body)  # 요청에서 JSON 데이터 파싱
					members_to_delete = data.get('members', [])
					# print("Members to delete:", members_to_delete)

					# 실제로 데이터베이스에서 삭제
					for member_id in members_to_delete:
							Administrator.objects.filter(id=member_id).delete()

					return JsonResponse({'status': 'success'}, status=200)
			except Exception as e:
					return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
	return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)


# 공지사항 리스트
def admin_noticeList(request):
	qs = NoticeBoard.objects.filter(category=1).order_by("-bno")
	context = {"notiList":qs}
	return render(request, 'admin_noticeList.html', context)

# 공지사항 쓰기
def admin_notiWrite(request):
	if request.method == 'GET':
		return render(request, 'admin_notiWrite.html')
	else:
		id = request.session.get('session_id')
		member = Administrator.objects.get(id=id)
		btitle = request.POST.get("title")
		bcontent = request.POST.get("content")
		bfile = request.FILES.get('bfile','')
		category = 1
		NoticeBoard.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile=bfile,category=category)
		context = {'wmsg':'1'}
		return render(request, 'admin_noticeList.html', context)


# 포스트 리스트
def admin_postList(request):
	return render(request, 'admin_postList.html')


# 포스트 쓰기
def admin_postWrite(request):
	if request.method == 'GET':
		return render(request, 'admin_postWrite.html')
	else:
		id = request.session.get('session_id')
		member = Administrator.objects.get(id=id)
		btitle = request.POST.get("title")
		bcontent = request.POST.get("content")
		bfile = request.FILES.get('bfile','')
		bfile_thumbnail = request.FILES.get('bfile_thumbnail','')
		category = 2
		NoticeBoard.objects.create(member=member,btitle=btitle,bcontent=bcontent,bfile_thumbnail=bfile_thumbnail,bfile=bfile,category=category)
		context = {'wmsg':'1'}
		return render(request, 'admin_noticeList.html', context)