from django.shortcuts import render, redirect
from accounts.models import Dog

# Create your views here.

def topPage(request):
    if request.user.is_authenticated:
        return redirect('myhp:index')
    else:
        return render(request, 'myhp/topPage.html', {})

def index(request):
    headLine = 'ユーザー一覧'
    objs = Dog.objects.order_by('-id')
    dog = Dog.objects.filter(user_id=request.user.id)
    if dog.count() == 0:
        dog_flg = 0
    else:
        dog_flg = 1
    return render(request, 'myhp/index.html', {
        'headLine': headLine,
        'objs': objs,
        'dog_flg': dog_flg,
    })