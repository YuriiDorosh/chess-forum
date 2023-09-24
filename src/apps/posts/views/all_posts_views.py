from django.shortcuts import render
from posts.models import UserPost

def all_user_posts(request):
    posts = UserPost.objects.all().order_by('-date_added')
    return render(request, 'posts/all_user_posts.html', {'posts': posts})
