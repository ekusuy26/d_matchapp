from django.contrib.auth import forms as auth_forms
from django import forms
from .models import Chat

class ChatForm(forms.ModelForm):
    class Meta:
        model = Chat
        fields = ('text',)
