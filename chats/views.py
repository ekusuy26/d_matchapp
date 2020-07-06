from django.shortcuts import render
from chats.models import Party

# Create your views here.

def index(request):
    parties = Party.objects.filter(users=request.user.id)
    return render(request, 'chats/index.html', {
        'parties' : parties
        })