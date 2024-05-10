from django.urls import path
from .views import *

urlpatterns = [
    path('create-list/', TodoAPIVew.as_view() ),
    path('manage/<int:id>/', ManageTodoAPIView.as_view())
]
