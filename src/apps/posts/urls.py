from django.urls import path
from posts.views import (action_on_the_post_views, all_posts_views,
                         like_posts_views)

app_name = "posts"

urlpatterns = [
    path("", all_posts_views.all_user_posts, name="all_user_posts"),
    path("create/", action_on_the_post_views.CreateUserPostView.as_view(), name="create_post"),
    path("edit/<uuid:post_id>/", action_on_the_post_views.EditUserPostView.as_view(), name="edit_post"),
    path("like/<uuid:post_id>/", like_posts_views.LikePostView.as_view(), name="like_post"),
]
