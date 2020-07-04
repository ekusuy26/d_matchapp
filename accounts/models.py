from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Dog(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dogname = models.CharField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=100)
    introduction = models.CharField(max_length=255)
    image = models.ImageField(upload_to="dogs/")
    like_num = models.IntegerField(default=0)