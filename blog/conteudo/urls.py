from django.urls import path
from .views import index, posts

urlpatterns = [
    path('', index, name="index"),
    path('home/', index, name="index"),
    path('<int:post>', posts, name="posts"),
]
