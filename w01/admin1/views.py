from django.shortcuts import render
from admin1.models import Administrator

def admin_login(request):
	if request.method == 'GET':
		return render(request, 'admin_login.html')
	else:
		id = request.POST.get('user_id')
		pw = request.POST.get('user_pw')

		qs = Administrator.objects.filter(id=id,pw=pw)
		if qs:
			request.session['session_id']
			context = {'lmsg':'1'}
		else:
			context = {'lmsg':'0'}
		return render(request, 'admin_login.html', context)
	
def admin_memList(request):
	return render(request, 'admin_memList.html')
