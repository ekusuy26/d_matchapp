from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Party(models.Model):
    users = models.ManyToManyField(User, verbose_name='ユーザー')
    name = models.CharField(max_length=20)

class Chat(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    uploaded_at = models.DateTimeField(auto_now_add=True)
