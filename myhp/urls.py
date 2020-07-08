from django.urls import path
from . import views
 
app_name='myhp'
 
urlpatterns = [
    path('', views.topPage, name='topPage'),
    path('index/', views.index, name='index'),
    path('fusion/<int:pk>/', views.fusion, name='fusion'),
]
