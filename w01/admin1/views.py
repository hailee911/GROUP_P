from django.shortcuts import render,redirect
from admin1.models import Administrator
from loginpage.models import Member

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

# 관리자 리스트
def admin_adminList(request):
	return render(request, 'admin_adminList.html')