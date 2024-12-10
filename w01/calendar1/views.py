from django.shortcuts import render
from calendar1.models import Event

# 테스트
def test1(request):
  context = {'message': '이것은 서버에서 전달된 메시지입니다.'}
  return render(request,'test1.html', context)

# 캘린더
def cal(request):
  if request.method == "POST":
    title = request.POST.get('title')
    start_date = request.POST.get('start_date')
    end_date = request.POST.get('end_date')
    location = request.POST.get('location')
    repeat = request.POST.get('repeat')
    memo = request.POST.get('memo')
    Event.objects.create(
      title=title,
      start_date=start_date,
      end_date=end_date,
      location=location,
      repeat=repeat,
      memo=memo,
    )
    return render(request,'calendar.html')
  else:
    return render(request,'calendar.html')