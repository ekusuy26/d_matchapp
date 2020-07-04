from django.shortcuts import render
from accounts.models import Dog

# Create your views here.

def topPage(request):
    return render(request, 'myhp/topPage.html', {})

def index(request):
    dog = Dog.objects.filter(user_id=request.user.id)
    if dog.count() == 0:
        dog_flg = 0
    else:
        dog_flg = 1
    return render(request, 'myhp/index.html', {
        'dog_flg': dog_flg,
    })