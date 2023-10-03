from django.shortcuts import get_object_or_404, redirect
from django.views import View
from posts.models.post import UserPost
from posts.models.post_likes import Like
from posts.services.like_post_service import LikeService

class LikePostView(View):
    """
    View for handling the liking/unliking of a user post.

    Methods:
        post(self, request, post_id): Handles POST requests to like/unlike a post.

    Attributes:
        None
    """

    def post(self, request, post_id):
        """
        Handles POST requests to like/unlike a user post.

        Args:
            request: The HTTP request.
            post_id: The ID of the post being liked/unliked.

        Returns:
            HttpResponseRedirect: Redirects to the previous page after the action.
        """
        post = get_object_or_404(UserPost, id=post_id)
        created = LikeService.toggle_like(request.user, post_id)

        previous_page = request.META.get("HTTP_REFERER", None)


        return redirect(previous_page or "posts:all_user_posts")
