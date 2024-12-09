from django.shortcuts import render

# Create your views here.
def main(request):
  return render(request, 'mymain.html')

def modify(request):
  return render(request, 'mypage_modi.html')