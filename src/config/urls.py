from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from apps.posts.views import all_posts_views

urlpatterns = [
    path("", all_posts_views.all_user_posts, name="home"),
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),
    path("posts/", include("posts.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
