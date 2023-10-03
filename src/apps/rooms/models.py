from django.db import models

from core.models import BaseModel


class Room(BaseModel):
    """
    Model representing a chat room.

    Attributes:
        name (CharField): The name of the room (max length 30 characters).
        slug (SlugField): A unique identifier for the room in slug format.
        premium (BooleanField): A flag indicating whether the room is a premium room (default is False).

    """

    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(unique=True)
    premium = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"Room: {self.name}"
