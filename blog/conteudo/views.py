from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    context = {"post": Post.objects.all()[0:5]}
    return render(request, "conteudo/index.html", context=context)


def posts(request, post):
    context = {'post': Post.objects.all()[post-1]}
    return render(request, "conteudo/post.html", context=context)
