from discussions.models.discussion import Discussion
from discussions.models.reply import Reply
from discussions.models.reply_like import ReplyLike
from django.contrib import admin
from posts.models.post import UserPost
from posts.models.post_likes import Like
from room_messages.models.message import Message
from rooms.models.room import Room
from users.models.user import User


class UserAdmin(admin.ModelAdmin):
    pass


class UserPostAdmin(admin.ModelAdmin):
    pass


class LikeAdmin(admin.ModelAdmin):
    pass


class RoomAdmin(admin.ModelAdmin):
    pass


class MessageAdmin(admin.ModelAdmin):
    pass


class DiscussionAdmin(admin.ModelAdmin):
    pass


class ReplyAdmin(admin.ModelAdmin):
    pass


class ReplyLikeAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(UserPost, UserPostAdmin)
admin.site.register(Like, LikeAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Discussion, DiscussionAdmin)
admin.site.register(Reply, ReplyAdmin)
admin.site.register(ReplyLike, ReplyLikeAdmin)
