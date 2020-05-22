from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

from blog.models import Category, Post

import logging

logger = logging.getLogger('blog')


def index(req):
    logger.info("log level : info / view > index")
    post_latest = Post.objects.order_by("-createDate")[:5]      # 내림차순
    context = {
        "post_latest": post_latest
    }

    return render(req, 'index.html', context=context)


class PostDetailView(generic.DetailView):
    logger.error("log level : ERROR / view > DetailView")
    model = Post


class PostCreate(LoginRequiredMixin, CreateView):
    logger.error("log level : ERROR / view > CreateView")
    model = Post
    fields = ['title', 'title_image', 'content', 'category']


def post_list(req):
    logger.info("log level : info / view > post_list")
    page = int(req.GET.get('page', '1'))
    posts = Post.objects.order_by("-createDate")

    paginator = Paginator(posts, 10)
    page_obj = paginator.get_page(page)

    context = {
        'posts': page_obj
    }

    return render(req, 'blog/post_list.html', context=context)


def post_video(req):
    return render(req, 'blog/post_video.html')


def error404(request, exception):
    return render(request, "404.html", status=404)


def error500(request):
    return render(request, "500.html", status=500)
