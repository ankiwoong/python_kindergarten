from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

from blog.models import Category, Post

# Create your views here.


def index(req):
    post_latest = Post.objects.order_by("-createDate")[:]      # 내림차순
    context = {
        "post_latest": post_latest
    }

    return render(req, 'index.html', context=context)


class PostDetailView(generic.DetailView):
    model = Post


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'title_image', 'content', 'category']


def post_list(req):
    page = int(req.GET.get('page', '1'))
    posts = Post.objects.order_by("-createDate")

    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(page)

    context = {
        'posts': page_obj
    }

    return render(req, 'blog/post_list.html', context=context)
