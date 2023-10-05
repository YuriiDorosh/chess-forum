from discussions.models.discussion import Discussion
from django.db.models import Count
from django.shortcuts import render
from posts.models.post import UserPost


def home(request):
    top_posts = UserPost.objects.annotate(like_count=Count("likes")).order_by(
        "-like_count"
    )[:10]

    open_discussions = Discussion.objects.filter(closed=False)

    context = {
        "top_posts": top_posts,
        "open_discussions": open_discussions,
    }

    return render(request, "core/home.html", context)
