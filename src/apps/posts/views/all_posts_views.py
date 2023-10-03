from django.db.models import Count
from django.shortcuts import render
from posts.models import UserPost


def all_user_posts(request):
    sort = request.GET.get("sort")

    if sort == "newest":
        posts = UserPost.objects.all().order_by("-date_added").annotate(likes_count=Count("likes"))
    elif sort == "most_likes":
        posts = UserPost.objects.all().annotate(likes_count=Count("likes")).order_by("-likes_count")
    else:
        posts = UserPost.objects.all().annotate(likes_count=Count("likes"))

    return render(request, "posts/all_user_posts.html", {"posts": posts})
