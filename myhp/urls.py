from django.urls import path
from . import views
 
app_name='myhp'
 
urlpatterns = [
    path('', views.toppage, name='toppage'),
]
