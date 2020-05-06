#Yipeng Niu yn2371
from django.urls import path
from . import views

urlpatterns = [
        path('', views.index),
]
