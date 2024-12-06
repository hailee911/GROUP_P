from django.shortcuts import render
from customer.models import NoticeBoard

# Create your views here.
def main(request):
  qs = NoticeBoard.objects.order_by('-bno')[:5]
  context = {'notice_5':qs}
  return render(request, 'customer_service.html', context)

def noticelist(request):
  qs = NoticeBoard.objects.all().order_by('-bno')
  context = {'notice_list':qs}
  return render(request, 'customer_notice_list.html', context)

def noticeview(request, bno):
  qs = NoticeBoard.objects.get(bno=bno)
  context = {'view':qs}
  return render(request, 'customer_notice_view.html', context)