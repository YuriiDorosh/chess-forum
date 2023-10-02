from django.db import models
from versatileimagefield.fields import VersatileImageField

from users.models import User
from core.models import BaseModel

class Discussion(BaseModel):
    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = VersatileImageField(null=True, blank=True, upload_to="images")
    closed = models.BooleanField(default=False)


    def __str__(self):
        return self.title

class Reply(BaseModel):
    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name='replies')
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = VersatileImageField(null=True, blank=True, upload_to="images")


    def __str__(self):
        return f'Reply to "{self.discussion.title}"'


class ReplyLike(BaseModel):
    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Like by {self.user.username} on Reply {self.reply.id}'