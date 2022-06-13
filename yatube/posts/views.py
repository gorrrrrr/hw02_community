from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def index(request):
    template = 'posts/index.html'
    post_number = 10  # постов на странице
    posts = Post.objects.filter()[:post_number]
    context = {
        'posts': posts,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)

    post_number = 10  # постов на странице

    posts = Post.objects.filter(group=group)[:post_number]
    # пока что ничерта не понял про _set.all() :(
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)
