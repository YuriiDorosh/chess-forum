from django.shortcuts import get_object_or_404
from posts.models.post import UserPost
from posts.models.post_likes import Like

class LikeService:
    @staticmethod
    def toggle_like(user, post_id):
        post = get_object_or_404(UserPost, id=post_id)
        like, created = Like.objects.get_or_create(user=user, post=post)

        if not created:
            like.delete()

        return created
