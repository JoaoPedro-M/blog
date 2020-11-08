from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    posts = Post.objects.all()[0:5]
    for post in posts:
        if '    ' in post.conteudo:
            post.conteudo = post.conteudo.replace('    ', '</p><p>')
    context = {"post": posts}
    return render(request, "conteudo/index.html", context=context)


def posts(request, post):
    pos = Post.objects.all()[post-1]
    if '    ' in pos.conteudo:
        pos.conteudo = pos.conteudo.replace('    ', '</p><p>')
    context = {'post': pos}
    return render(request, "conteudo/post.html", context=context)
