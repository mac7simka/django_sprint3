from django.shortcuts import render


def index(request):
    template_name = 'blog/index.html'
    context = {}
    return render(request, template_name, context)


def post_detail(request, id):
    pk = id
    template_name = 'blog/detail.html'
    context = {}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    template_name = 'blog/category.html'
    context = category_slug
    return render(request, template_name, context)
