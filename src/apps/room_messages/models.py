from django.db import models
from users.models import User
from rooms.models import Room


class Message(models.Model):
    """
    A model representing messages posted within chat rooms.

    Attributes:
        room (Room): The chat room where the message is posted.
        user (User): The user who posted the message.
        content (str): The content of the message.
        date_added (datetime): The date and time when the message was added (auto-generated).
    """

    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)