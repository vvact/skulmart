from django.shortcuts import render
from rest_framework import viewsets
from .models import CustomUser
from .serilizers import CustomUserSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

