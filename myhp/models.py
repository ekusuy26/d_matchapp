from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Image(models.Model):
    users = models.ManyToManyField(User, verbose_name='ユーザー')
    first_image = models.ImageField(upload_to='results/', default='defo')
    second_image = models.ImageField(upload_to='results/', default='defo')
    uploaded_at = models.DateTimeField(auto_now_add=True)
