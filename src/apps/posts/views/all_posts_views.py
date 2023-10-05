from django.db.models import Count
from django.shortcuts import render
from django.views import View
from posts.models.post import UserPost


class AllUserPostsView(View):
    """
    View for displaying all user posts with sorting options.

    Attributes:
        template_name (str): The path to the HTML template for displaying the list of user posts.

    Methods:
        get(self, request): Handles GET requests and displays the list of user posts based on sorting.

    Template:
        posts/all_user_posts.html
    """

    template_name = "posts/all_user_posts.html"

    def get(self, request):
        """
        Handles GET requests and displays the list of user posts based on sorting.

        Args:
            request: The HTTP request.

        Returns:
            HttpResponse: Response with a list of user posts.
        """
        sort = request.GET.get("sort")

        if sort == "newest":
            posts = (
                UserPost.objects.all()
                .order_by("-date_added")
                .annotate(likes_count=Count("likes"))
            )
        elif sort == "most_likes":
            posts = (
                UserPost.objects.all()
                .annotate(likes_count=Count("likes"))
                .order_by("-likes_count")
            )
        else:
            posts = UserPost.objects.all().annotate(likes_count=Count("likes"))

        return render(request, self.template_name, {"posts": posts})
