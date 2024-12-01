from django.shortcuts import render
from.models import Blog_Post
from django.http import HttpResponseRedirect, HttpResponseNotFound
# Create your views here.

def index(request):
    all_data = Blog_Post.objects.all()
    return render(request, 'index.html', {'all_data': all_data})

def create(request):
    if request.method == 'POST':
        post = Blog_Post()
        post.title = request.POST.get('title')
        post.text = request.POST.get('text')
        post.thema = request.POST.get('thema')
        post.save()
    return HttpResponseRedirect('/')

def edit(request, id):
    try:
        post = Blog_Post.objects.get(id=id)

        if request.method == 'POST':
            post.title = request.POST.get('title')
            post.text = request.POST.get('text')
            post.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'edit.html', {'post': post})
    except Blog_Post.DoesNotExist:
        return HttpResponseNotFound('<h2>Пост не найден</h2>')


def delete(request, id):
    try:
        if request.method == 'POST':
            post = Blog_Post.objects.get(id=id)
            post.delete()
            return HttpResponseRedirect('/')
    except Blog_Post.DoesNotExist:
        return HttpResponseNotFound('<h2>Пост не найден</h2>')