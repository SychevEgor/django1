from django.urls import path
from apppdjang2 import views

urlpatterns = [
    path('', views.index),
]