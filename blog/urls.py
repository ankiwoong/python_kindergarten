from django.urls import path
from blog import views

urlpatterns = [
    # 사이트 명이 입력이 안될시 index라는 것으로 처리 한다.
    # blog > views.py
    path('', views.index, name='index'),
    path('single/', views.single, name='single'),
]
