from django.shortcuts import render
from .serializers import *
from rest_framework import generics,status
from rest_framework.response import Response

# Create your views here.
class UserAPIView(generics.CreateAPIView):
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        response =  super().create(request, *args, **kwargs)
        
        return Response(response.data, status=status.HTTP_201_CREATED)

class LoginAPIView(generics.CreateAPIView):
    serializer_class = LoginSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data= request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status= status.HTTP_200_OK)