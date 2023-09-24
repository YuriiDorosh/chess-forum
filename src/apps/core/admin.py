from django.contrib import admin

from users.models import User
from posts.models import UserPost
from rooms.models import Room
from room_messages.models import Message

class UserAdmin(admin.ModelAdmin):
    pass

class UserPostAdmin(admin.ModelAdmin):
    pass

class RoomAdmin(admin.ModelAdmin):
    pass

class MessageAdmin(admin.ModelAdmin):
    pass




admin.site.register(User, UserAdmin)
admin.site.register(UserPost, UserPostAdmin)
admin.site.register(Room, RoomAdmin)
admin.site.register(Message, MessageAdmin)