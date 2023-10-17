from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.conf import settings
import os
from BlogsContent.models import category, post, project

# Create your views here.
def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def projects(request):
    myProject = project.objects.all().values()
    data ={
        "myProject": myProject,
    }
    print(data)
    return render(request, 'projects.html', data)

def singleposts(request, post_id):
    singlepost= post.objects.get(post_id=post_id)
    data ={
        'post_id' : post_id,
        'singlepost': singlepost,
    }
    return render(request, 'singlepost.html', data)

def blogs(request):
    posts = post.objects.all().values()
    cats = category.objects.all()
    data = {
        'posts' : posts,
        'cats' : cats
    }
    
    return render(request, 'blogs.html', data )

def categoryView(request, cat_id):
    category_posts = post.objects.values().filter(cat_id=cat_id)
    data ={
        'category_posts': category_posts,
        'cat_id' : cat_id,
    }
    
    return render(request, 'post.html', data)