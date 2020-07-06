from django.urls import path
from . import views
 
app_name='messages'
 
urlpatterns = [
    path('messages/index/', views.index, name="index"),
]
