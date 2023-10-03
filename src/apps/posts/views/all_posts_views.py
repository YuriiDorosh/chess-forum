from django.db.models import Count
from django.shortcuts import render
from django.views import View
from posts.models.post import UserPost

class AllUserPostsView(View):
    template_name = "posts/all_user_posts.html"

    def get(self, request):
        sort = request.GET.get("sort")

        if sort == "newest":
            posts = UserPost.objects.all().order_by("-date_added").annotate(likes_count=Count("likes"))
        elif sort == "most_likes":
            posts = UserPost.objects.all().annotate(likes_count=Count("likes")).order_by("-likes_count")
        else:
            posts = UserPost.objects.all().annotate(likes_count=Count("likes"))

        return render(request, self.template_name, {"posts": posts})
