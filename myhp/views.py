from django.shortcuts import render, redirect
from accounts.models import Dog
from django.core.paginator import Paginator

# Create your views here.

def topPage(request):
    if request.user.is_authenticated:
        return redirect('myhp:index')
    else:
        return render(request, 'myhp/topPage.html', {})

def index(request):
    headLine = 'ユーザー一覧'
    all_objs = Dog.objects.order_by('-id')
    paginator = Paginator(all_objs, 12) # 1ページに12件表示
    p = request.GET.get('p') # URLのパラメータから現在のページ番号を取得
    objs = paginator.get_page(p) # 指定のページのDogを取得
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

def fusion(request, pk):
    opponent = Dog.objects.get(id = pk)
    headLine = '合成してみる'
    return render(request, 'myhp/fusion.html', {
        'opponent': opponent,
        'headLine': headLine,
    })