from django.shortcuts import render

# Create your views here.
def main(request):
  return render(request, 'customer_service.html')

def noticelist(request):
  return render(request, 'customer_notice_list.html')

def noticeview(request):
  return render(request, 'customer_notice_view.html')