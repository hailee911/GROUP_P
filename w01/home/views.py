from django.shortcuts import render

def landing(request):
  return render(request,'landing.html')

def main(request):
  return render(request, 'main_navi_base.html')