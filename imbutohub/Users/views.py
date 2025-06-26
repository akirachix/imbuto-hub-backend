# from django.shortcuts import render

# # Create your views here.
# from rest_framework import viewsets
# from .models import User
# from .serializer import UserSerializer

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


from django.shortcuts import render
from rest_framework import viewsets
from Users.models import User
from api.serializer import UserSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer