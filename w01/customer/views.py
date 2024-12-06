from django.shortcuts import render
from customer.models import NoticeBoard

# Create your views here.
def main(request):
  return render(request, 'customer_service.html')

def noticelist(request):
  qs = NoticeBoard.objects.all()
  context = {'notice_list':qs}
  return render(request, 'customer_notice_list.html', context)

def noticeview(request, bno):
  qs = NoticeBoard.objects.get(bno=bno)
  context = {'view':qs}
  return render(request, 'customer_notice_view.html', context)