from django.urls import path, include
from django.http import HttpResponse
from rest_framework.routers import DefaultRouter
from .api import *

urlpatterns = [
    path('users/', UserAPIView.as_view()),
    path('users/<int:pk>/', UserAPIView.as_view()),
    path('products/', productAPIView.as_view()),
    path('products/<int:pk>/', productAPIView.as_view()),
]
































































































