from django.shortcuts import render, get_object_or_404
from yatube.settings import POST_NUMBER
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.filter()[:POST_NUMBER]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group_list = get_object_or_404(Group, slug=slug)
    post_list = group_list.posts.all()[:POST_NUMBER]
    context = {
        'group': group_list,
        'posts': post_list,
    }
    return render(request, template, context)
