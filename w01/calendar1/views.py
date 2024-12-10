from django.shortcuts import render
from calendar1.models import Event

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
