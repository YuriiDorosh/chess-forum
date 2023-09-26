from django.shortcuts import get_object_or_404, redirect
from django.views import View
from posts.models import UserPost
from posts.models import Like


class LikePostView(View):
    def post(self, request, post_id):
        post = get_object_or_404(UserPost, id=post_id)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        previous_page = request.META.get("HTTP_REFERER", None)

        if not created:
            like.delete()
        # return redirect('posts:all_user_posts')

        return redirect(previous_page or "posts:all_user_posts")
