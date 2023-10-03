from core.models import BaseModel
from django.db import models
from users.models.user import User
from versatileimagefield.fields import VersatileImageField


class Discussion(BaseModel):
    """
    A model representing a discussion.

    Attributes:
        title (str): The title of the discussion.
        text (str): The text content of the discussion.
        author (User): The user who authored the discussion.
        image (VersatileImageField): An optional image associated with the discussion.
        closed (bool): A flag indicating if the discussion is closed or not.

    Methods:
        __str__(): Returns the title of the discussion as a string.

    """

    title = models.CharField(max_length=255)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = VersatileImageField(null=True, blank=True, upload_to="images")
    closed = models.BooleanField(default=False)

    def __str__(self):
        return self.title





