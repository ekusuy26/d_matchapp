from django.shortcuts import render

# Create your views here.

def topPage(request):
    return render(request, 'myhp/topPage.html', {})