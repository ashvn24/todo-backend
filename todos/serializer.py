from rest_framework import serializers
from .models import Todos

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todos
        fields = ['id', 'user', 'todo', 'completed']
        extra_kwargs ={
            "user": {"read_only": True}
        }
        
