from django.urls import path
from . import views
 
app_name='chats'
 
urlpatterns = [
    path('chats/index/', views.index, name="index"),
    path('chats/show/<int:id>', views.show, name='show'),
]
