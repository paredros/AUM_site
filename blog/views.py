from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .models import *
from django.utils import timezone
import datetime
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def viewallblogs(request):
    dt = datetime.datetime.now().timestamp()
    posts = get_list_or_404(Post, enabled=True)
    page = request.GET.get('page')
    paginator = Paginator(posts, 2)
    posts_page = paginator.get_page(page)
    return render(request,'blog/listall.html', {'posts':posts_page, 'timestamp':dt})

def post(request, id_slug):
    dt = datetime.datetime.now().timestamp()
    post = get_object_or_404(Post, slug=id_slug)
    return render(request, 'blog/viewpost.html', {'post': post, 'timestamp': dt})