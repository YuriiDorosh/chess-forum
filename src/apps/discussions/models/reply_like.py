from core.models import BaseModel
from discussions.models.reply import Reply
from django.db import models
from users.models.user import User


class ReplyLike(BaseModel):
    """
    A model representing a like on a reply.

    Attributes:
        reply (Reply): The reply that received the like.
        user (User): The user who liked the reply.

    Methods:
        __str__(): Returns a string representation of the like.

    """

    reply = models.ForeignKey(Reply, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"Like by {self.user.username} on Reply {self.reply.id}"
