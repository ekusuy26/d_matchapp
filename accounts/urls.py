from django.urls import path
from . import views
 
app_name='accounts'
 
urlpatterns = [
    path('accounts/login/', views.MyLoginView.as_view(), name="login"),
    path('accounts/logout/', views.MyLogoutView.as_view(), name="logout"),
    path('accounts/create/', views.UserCreateView.as_view(),name="create"),
    path('dogs/new/', views.dogNew,name="dogNew"),
    path('dogs/update/<int:pk>/', views.DogUpdate.as_view(),name="dogUpdate"),
    path('dogs/delete/<int:pk>/', views.dogDelete,name="dogDelete"),
    path('dog/show/<int:pk>/', views.dogShow, name='dogShow'),
    path('like/<int:pk>/', views.like, name='like'),
    path('likedperson/', views.likedPerson, name='likedPerson'),
    path('likedopponent/', views.likedOpponent, name='likedOpponent'),
]
