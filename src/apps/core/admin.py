from django.contrib import admin

from users.models import User
from posts.models import UserPost, Like
from rooms.models import Room
from room_messages.models import Message
from discussions.models import Discussion, Reply, ReplyLike


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
