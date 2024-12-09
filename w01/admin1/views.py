from django.shortcuts import render
from admin1.models import Administrator
from loginpage.models import Member

# 관리자1 로그인
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
	
# 관리자 리스트
def admin_adminList(request):
	return render(request, 'admin_adminList.html')

# 회원관리 (유저리스트)
def admin_memList(request):
	qs = Member.objects.all()
	
	if qs:
		context = {'memlist':qs}
	else:
		context = {'msg':'멤버가 없습니다.'}
	return render(request, 'admin_memList.html', context)

# 회원 추가
def admin_memAdd(request):
	# 페이지 열기
	if request.method == 'GET':
		return render(request, 'admin_memAdd.html')
	# post 방식 (데이터 받기)
	else:
		id = request.POST.get('user_id')
		print(id)


# 포스트 리스트
def admin_postList(request):
	return render(request, 'admin_postList.html')

# 공지사항 리스트
def admin_noticeList(request):
	return render(request, 'admin_noticeList.html')

# 공지사항 글쓰기
def admin_notiWrite(request):
	return render(request, 'admin_notiWrite.html')