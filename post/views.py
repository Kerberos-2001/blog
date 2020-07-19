from django.shortcuts import render
from .models import Blog
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'post/index.html')

def BlogView(request):
    blog = Blog.objects.all()
    context = {'obj': blog}
    return render(request, 'post/blog.html' , context)

def detailBlog(request, slug):
    blog = Blog.objects.get(slug=slug)
    print(type(blog))
    context = {'obj': blog}
    return render(request, 'post/detail.html' , context)

def addBlog(request):
    if request.method == 'POST':
        blog = blogForm(request.POST)
        title = blog.cleaned_data['title']
        body = blog.cleaned_data['body']
        count = 1
        image = blog.cleaned_data['image']
        auther = request.user
        print(title, body, image, auther)
        blog = Blog(
            title=title,
            body=body,
            count=count,
            image = image,
            auther = auther
        )  
        blog.save() 

    blog = blogForm()
    context = {'form':blog}
    return render(request, 'post/addBlog.html', context)