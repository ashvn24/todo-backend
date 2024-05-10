from django.db import models
from users.models import CustomUser

# Create your models here.

class Todos(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    todo = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    
    def  __str__(self):
        return self.todo