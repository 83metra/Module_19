from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.

from .models import Blog_Post

def posts(request):
    posts = Blog_Post.objects.all().order_by('-created_at')
    posts_in_page = request.GET.get('posts_in_page', 3)
    paginator = Paginator(posts, posts_in_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'posts_in_page': posts_in_page
    }
    return render(request, 'posts.html', context)

