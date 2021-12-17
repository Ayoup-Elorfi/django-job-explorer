from django.shortcuts import render
from .models import Blog, Category
from django.core.paginator import Paginator
from .filters import BlogFilter


def blog_view(request):
    blog_object = Blog.objects.all()  # getting all blogs

    # using filter for user search
    blog_filter = BlogFilter(request.GET, queryset=blog_object)
    blog_object = blog_filter.qs

    # getting all categories to view in the page
    categories = Category.objects.all()

    # paginator
    paginator = Paginator(blog_object, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'blogs': page_obj,
        'categories': categories,
        'blog_filter': blog_filter,
    }
    return render(request, 'blogs/blogs.html', context)


def blog_detail_view(request, slug=None):
    single_blog = None
    if slug is not None:
        single_blog = Blog.objects.get(slug=slug)

    context = {
        'single_blog': single_blog
    }

    return render(request, 'blogs/detail.html', context=context)
