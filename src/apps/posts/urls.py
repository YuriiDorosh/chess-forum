from django.urls import path
from posts.views import all_posts_views

app_name = "posts"

urlpatterns = [
    path("all/", all_posts_views.all_user_posts, name="all_user_posts"),
]
