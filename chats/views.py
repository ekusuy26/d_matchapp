from django.shortcuts import render, loader, redirect
from django.http import HttpResponse
from chats.models import Party, Chat
from .forms import ChatForm

# Create your views here.

def index(request):
    parties = Party.objects.filter(users=request.user.id)
    return render(request, 'chats/index.html', {
        'parties' : parties
        })

def show(request, id):
    if request.method == 'GET':
        form = ChatForm()
    else:
        form = ChatForm(request.POST, request.FILES)
        form.instance.user_id = request.user.id
        form.instance.party_id = id
        if form.is_valid():
            print('chat_regist is_valid')
            form.save(request.POST)
            return redirect('/chats/show/' + str(id))
        else:
            print('chat_regist false is_valid')

    parties = Party.objects.filter(users=request.user.id)
    chats = Chat.objects.filter(party_id=id)
    template = loader.get_template('chats/show.html')
    context = {
        'form': form,
        'chats' : chats,
        'parties' : parties,
    }
    return HttpResponse(template.render(context, request))