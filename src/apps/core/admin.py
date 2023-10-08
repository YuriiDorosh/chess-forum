from discussions.models.discussion import Discussion
from discussions.models.reply import Reply
from discussions.models.reply_like import ReplyLike
from django.contrib import admin
from posts.models.post import UserPost, UserPostImage
from posts.models.post_likes import Like
from room_messages.models.message import Message
from rooms.models.room import Room
from users.models.user import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "subscriber")
    list_filter = ("subscriber",)


@admin.register(UserPost)
class UserPostAdmin(admin.ModelAdmin):
    list_display = ("user", "title", "date_added")
    list_filter = ("user", "date_added")
    search_fields = ("title", "body")


@admin.register(UserPostImage)
class UserPostImageAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "date_added")
    list_filter = ("user", "date_added")


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "premium")
    list_filter = ("premium",)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ("room", "user", "date_added")
    list_filter = ("room", "user", "date_added")


@admin.register(Discussion)
class DiscussionAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "closed")
    list_filter = ("author", "closed")
    search_fields = ("title", "text")


@admin.register(ReplyLike)
class ReplyLikeAdmin(admin.ModelAdmin):
    list_display = ("user", "reply")
    list_filter = ("user", "reply")


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    list_display = ("discussion", "author", "date_added")
    list_filter = ("discussion", "author", "date_added")
