from django.shortcuts import render
from .models import Post

# Create your views here.


def index(request):
    context = {"post": Post.objects.all()}
    return render(request, "conteudo/index.html", context=context)
