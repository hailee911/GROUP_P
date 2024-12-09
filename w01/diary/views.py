from django.shortcuts import render
from loginpage.models import Member
from diary.models import Letter
from django.http import JsonResponse

def diaryHome(request):
  qs = Letter.objects.all().order_by("ldate")
  letters = Letter.objects.filter(id=id).select_related('id')
  contents = Letter.objects.all().order_by("lno")
  member = Member.objects.filter(id=id)
  context = {"list":qs, "letters":letters, "contents":contents, 'member':member}
  return render(request,'diaryHome.html',context)

