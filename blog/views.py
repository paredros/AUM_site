from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from django.utils import timezone
import datetime

# Create your views here.
def viewallblogs(request):
    dt = datetime.datetime.now().timestamp()
    posts = get_list_or_404(Post)
    return render(request,'blog/listall.html', {'posts':posts, 'timestamp':dt})

def post(request, id_slug):
    dt = datetime.datetime.now().timestamp()
    post = get_object_or_404(Post, slug=id_slug)
    return render(request, 'blog/viewpost.html', {'post': post, 'timestamp': dt})