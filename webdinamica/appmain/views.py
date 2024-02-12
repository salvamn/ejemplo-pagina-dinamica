from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from appblogs.models import Post

# Create your views here.


@login_required
def inicio(request):
    # https://www.w3schools.com/django/django_queryset_orderby.php
    posts = Post.objects.all().order_by('-fecha_publicacion')
    print(posts)

    # for post in posts:
    #     print(post.imagen.name)
    #     print(type(post.imagen.name))
        # print(post.imagen.url)
        # print(post.imagen.chunks)
        # print(post.imagen.path)

    return render(request, 'inicio.dj', {'posts': posts})
