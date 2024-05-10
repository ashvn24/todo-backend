from django.shortcuts import render
from rest_framework import generics, status, pagination
from .serializer import TodoSerializer
from rest_framework.permissions import IsAuthenticated
from .models import Todos

# Create your views here.

class TodoPagination(pagination.PageNumberPagination):
    page_size = 10  # Set the number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100

class TodoAPIVew(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]
    # pagination_class = TodoPagination
    
    def perform_create(self, serializer):
        print(self.request.user)
        serializer.save(user=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        return Todos.objects.filter(user=user)
    
class ManageTodoAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    pagination_class = [IsAuthenticated]
    queryset = Todos.objects.all()
    lookup_field = 'id'
