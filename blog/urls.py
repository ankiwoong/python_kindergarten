from django.urls import path
from blog import views

# url 처리규칙
urlpatterns = [
    path('', views.index, name='index'),
    path("post/<int:pk>", views.PostDetailView.as_view(), name="post"),
    path("post/create", views.PostCreate.as_view(), name="post_create"),
    path('post/list/', views.post_list, name='post_list'),
    path('post/video/', views.post_video, name='post_video'),
]
