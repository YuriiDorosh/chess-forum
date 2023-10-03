from django import template
from posts.models.post_likes import Like

register = template.Library()


@register.filter
def has_liked_post(post, user):
    return Like.objects.filter(post=post, user=user).exists()
