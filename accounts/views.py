from django.shortcuts import render, loader, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView,CreateView,DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from . import forms
from .forms import DogForm
from django.http import HttpResponse
from .models import Dog, Like
from django.contrib.auth.models import Group, User
from chats.models import Party
from django.core.paginator import Paginator
from myhp.views import paginate_queryset

# Create your views here.

class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "accounts/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "myhp/topPage.html"

class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "accounts/create.html"
    success_url = reverse_lazy("accounts:login")

def dogNew(request):
    if request.method == 'GET':
        form = DogForm()
    else:
        form = DogForm(request.POST, request.FILES)
        form.instance.user_id = request.user.id
        if form.is_valid():
            print('dog_regist is_valid')
            form.save(request.POST)
            return redirect('myhp:index')
        else:
            print('dog_regist false is_valid')
    template = loader.get_template('accounts/dogNew.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))

class DogUpdate(UpdateView):
    template_name = 'accounts/dogNew.html'
    model = Dog
    fields = ['image', 'dogname', 'age', 'sex', 'introduction']
    success_url = reverse_lazy('myhp:index')

def dogDelete(request, pk):
    dog = Dog.objects.get(id=pk)
    dog.delete()
    return redirect('myhp:index')

def dogShow(request, pk):
    dog = Dog.objects.get(id = pk)
    query = Like.objects.filter(user_id=request.user.id, dog_id=pk)
    if query.count() == 0:
        like_flg = 0
    else:
        like_flg = 1
    return render(request, 'accounts/dogShow.html', {
        'dog': dog,
        'like_flg': like_flg,
        })

def like(request, pk):
    query = Like.objects.filter(user_id=request.user.id, dog_id=pk)
    if query.count() == 0:
        # いいねする処理
        likes_tbl = Like()
        likes_tbl.user_id = request.user.id
        likes_tbl.dog_id = pk
        likes_tbl.save()
        dog = Dog.objects.get(id = pk)
        dog.like_num += 1
        dog.save()
        # 相手が自分にいいねしているか確認
        opponent_id = Dog.objects.get(id=pk).user.id
        check = Like.objects.filter(user_id=opponent_id, dog_id=request.user.dog.id)
        if check.count() == query.count():
            try:
                max_id = Party.objects.latest('id').id
            except:
                max_id = 0
            parties_tbl = Party()
            parties_tbl.name = 'group' + str(max_id + 1)
            parties_tbl.save()
            new_party = Party.objects.latest('id')
            new_party.users.add(request.user)
            new_party.users.add(opponent_id)
            return redirect('/chats/index/')
    else:
        # いいね外す処理
        query.delete()
        dog = Dog.objects.get(id = pk)
        dog.like_num -= 1
        dog.save()
    return redirect('/dog/show/' + str(pk))

# いいねした相手
def likedPerson(request):
    all_objs = Like.objects.filter(user_id=request.user.id)
    objs = paginate_queryset(request, all_objs, 5)
    headLine = 'じぶんからのいいね！'
    return render(request, 'accounts/liked_person.html', {
        'objs': objs,
        'headLine': headLine,
    })

# いいねされた相手
def likedOpponent(request):
    all_objs = Like.objects.filter(dog_id=request.user.dog.id)
    objs = paginate_queryset(request, all_objs, 5)
    headLine = 'あいてからのいいね！'
    return render(request, 'accounts/liked_opponent.html', {
        'objs': objs,
        'headLine': headLine,
    })
