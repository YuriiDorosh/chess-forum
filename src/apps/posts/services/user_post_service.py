from django.shortcuts import get_object_or_404
from posts.models.post import UserPost


class UserPostService:
    @staticmethod
    def create_user_post(user, form_data):
        new_post = UserPost(
            user=user, title=form_data["title"], game_link=form_data["game_link"], body=form_data["body"]
        )
        new_post.save()
        return new_post

    @staticmethod
    def edit_user_post(post_id, user, form_data):
        post = get_object_or_404(UserPost, id=post_id, user=user)
        post.title = form_data["title"]
        post.game_link = form_data["game_link"]
        post.body = form_data["body"]
        post.save()
        return post
