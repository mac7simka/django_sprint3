from datetime import datetime

from django.shortcuts import get_object_or_404, render

from blog.models import Category, Post
from blogicum.constants import AMOUNT_POSTS


def index(request):
    template_name = 'blog/index.html'
    post_list = Post.published.filter(
        category__is_published=True,
        pub_date__date__lt=datetime.now())[:AMOUNT_POSTS]
    context = {'post_list': post_list}
    return render(request, template_name, context)


def post_detail(request, post_id):
    template_name = 'blog/detail.html'
    post = get_object_or_404(Post.published,
                             category__is_published=True,
                             pub_date__date__lt=datetime.now(),
                             pk=post_id)
    context = {
        'post': post,
    }
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    category = get_object_or_404(Category.published,
                                 slug=category_slug,
                                 )
    posts = category.posts.filter(
        is_published=True,
        pub_date__date__lt=datetime.now())

    context = {'category': category, 'post_list': posts}
    return render(request, template_name, context)
