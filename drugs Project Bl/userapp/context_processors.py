from .models import *
from django.shortcuts import render,redirect,get_object_or_404



def latest_posts(request):
    latest_posts = Post.objects.order_by('-timestamp')[:3]  
    return {
        'latest_posts': latest_posts
    }

