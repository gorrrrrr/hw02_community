from django.shortcuts import render, get_object_or_404
from yatube.settings import POST_NUMBER
from .models import Post, Group, User
from django.core.paginator import Paginator


def index(request):
    template = 'posts/index.html'
    posts = Post.objects.all()
    paginator = Paginator(posts, POST_NUMBER, allow_empty_first_page=False)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, template, context)


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group_list = get_object_or_404(Group, slug=slug)
    post_list = group_list.posts.all()
    paginator = Paginator(post_list, POST_NUMBER, allow_empty_first_page=False)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'group': group_list,
        'page_obj': page_obj,
    }
    return render(request, template, context)


def profile(request, username):
    template = 'posts/profile.html'
    author = get_object_or_404(User, username=username)
    post_list = author.posts.all()
    post_count = post_list.count()
    paginator = Paginator(post_list, POST_NUMBER, allow_empty_first_page=False)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'author': author,
        'page_obj': page_obj,
        'post_count': post_count,
    }
    return render(request, template, context)


def post_detail(request, post_id):
    template = 'posts/post_detail.html'
    post = get_object_or_404(Post, pk=post_id)
    post_count = Post.objects.filter(author=post.author).count()

    context = {'post': post, 'post_count': post_count}
    return render(request, template, context)
