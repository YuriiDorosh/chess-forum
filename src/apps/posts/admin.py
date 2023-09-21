from django.contrib import admin

from posts.models import UserPost


class UserPostAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserPost, UserPostAdmin)
