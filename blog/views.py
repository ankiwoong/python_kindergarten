from django.shortcuts import render
from django.views import generic

from blog.models import Category, Post

# Create your views here.


def index(req):
    post_latest = Post.objects.order_by("-createDate")[:6]      # 내림차순
    context = {
        "post_latest": post_latest
    }

    return render(req, 'index.html', context=context)


class PostDetailView(generic.DetailView):
    model = Post
