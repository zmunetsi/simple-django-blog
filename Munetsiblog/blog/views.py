from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse
from .models import Blogpost

def detail(request,Blogpost_id):
    post = Blogpost.objects.get(id=Blogpost_id)
    return render(request,"post.html", {"detail":post})
    
    

def blog(request):
    posts = Blogpost.objects.all()
    return render(request,"blog.html",{"posts":posts})

# Create your views here.
