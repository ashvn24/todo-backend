from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('token/refresh',TokenRefreshView.as_view(),name= 'token_refresh'),
    path('reg/', UserAPIView.as_view()),
    path('log/', LoginAPIView.as_view()),
    
]
