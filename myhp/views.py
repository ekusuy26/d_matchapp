from django.shortcuts import render

# Create your views here.

def topPage(request):
    return render(request, 'myhp/topPage.html', {})

def index(request):
    return render(request, 'myhp/index.html', {})