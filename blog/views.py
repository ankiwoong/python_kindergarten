from django.shortcuts import render

# Create your views here.

# index 처리


def index(req):
    context = {

    }

    return render(req, 'index.html', context=context)


def single(req):
    context = {

    }

    return render(req, 'single.html', context=context)
