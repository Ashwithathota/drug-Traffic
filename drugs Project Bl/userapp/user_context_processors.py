from .models import *
from django.shortcuts import render,redirect,get_object_or_404



def user_context(request):
    try:
        user_id = request.session.get('user_id_after_login')
        user = get_object_or_404(User, pk=user_id)
        
        posts_count = Post.objects.filter(user=user).count()
        
        return {
            'user_det': user,
            'posts_count': posts_count,
        }
    except Exception as e:
        return {
            'user_det': None,
            'posts_count': 0,
        }