from django.urls import path
from blog import views

# url 처리규칙
urlpatterns = [
    path('', views.index, name='index'),
    path('single/', views.single, name='single'),
]
