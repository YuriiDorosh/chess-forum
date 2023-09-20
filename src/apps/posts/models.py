from django.db import models
from users.models import User


class UserPost(models.Model):
    """
    A model representing user posts on the posts page and profile.

    Attributes:
        user (ForeignKey): The user who created the post.
        title (CharField): The title of the post (limited to 100 characters).
        game_link (URLField, optional): A link to a chess game related to the post (optional).
        body (TextField): The main content of the post.
        date_added (DateTimeField): The date and time when the post was created.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    game_link = models.URLField(max_length=60, blank=True, null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
