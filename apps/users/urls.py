from django.urls import path
from .views import registerUser, getUserProfile, getUsers, MyTokenObtainPairView
from . import views

urlpatterns = [
    path('users/login/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/register/', views.registerUser, name='registerUser'),
    path('users/profile/', views.getUserProfile, name='getUserProfile'),
    path('users/', views.getUsers, name='getUsers'),
]
