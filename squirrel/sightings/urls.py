#Yipeng Niu yn2371
from django.urls import path, re_path
from . import views

urlpatterns = [
        path('', views.index),
        path('add/', views.add),
        path('stats/', views.stats),
        re_path(r'(?P,uer_id>\d+[A-Z]-[A-Z]{2}-\d{4}-\d{9})/', views.s_id)
        ]
