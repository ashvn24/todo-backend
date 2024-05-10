from django.shortcuts import render
from rest_framework import generics, status
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Todo
# Create your views here.


class TodoAPIVew(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(user=user)
