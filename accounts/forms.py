from django.contrib.auth import forms as auth_forms
from django import forms
from .models import Dog

class LoginForm(auth_forms.AuthenticationForm):
    '''ログインフォーム'''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['placeholder'] = field.label

class DogForm(forms.ModelForm):
    class Meta:
        model = Dog
        fields = ('image', 'dogname', 'age', 'sex', 'introduction',)