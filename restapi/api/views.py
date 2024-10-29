#from django.shortcuts import render
from rest_framework import generics
from .models import User
from .serializers import UserSerializer

class UserListCreateView(generics.ListCreateAPIView):
    """
    View to list all users or create a new user.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    View to retrieve, update, or delete a user by ID.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
