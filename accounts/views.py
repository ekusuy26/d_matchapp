from django.shortcuts import render, loader, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import TemplateView,CreateView,DeleteView, UpdateView
from django.urls import reverse_lazy, reverse
from . import forms
from .forms import DogForm
from django.http import HttpResponse

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
            return redirect('myhp:toppage')
        else:
            print('dog_regist false is_valid')
    template = loader.get_template('accounts/dogNew.html')
    context = {
        'form': form,
    }
    return HttpResponse(template.render(context, request))