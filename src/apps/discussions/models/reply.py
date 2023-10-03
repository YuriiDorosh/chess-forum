from core.models import BaseModel
from discussions.models.discussion import Discussion
from django.db import models
from users.models.user import User
from versatileimagefield.fields import VersatileImageField


class Reply(BaseModel):
    """
    A model representing a reply to a discussion.

    Attributes:
        discussion (Discussion): The discussion to which the reply belongs.
        text (str): The text content of the reply.
        author (User): The user who authored the reply.
        image (VersatileImageField): An optional image associated with the reply.

    Methods:
        __str__(): Returns a string representation of the reply.

    """

    discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE, related_name="replies")
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = VersatileImageField(null=True, blank=True, upload_to="images")

    def __str__(self):
        return f'Reply to "{self.discussion.title}"'
