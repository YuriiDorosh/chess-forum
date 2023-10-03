from core.models import BaseModel
from core.validators import validate_chess_game_url
from django.db import models
from users.models.user import User


class UserPost(BaseModel):
    """
    A model representing user posts on the posts page and profile.

    Attributes:
        user (ForeignKey): The user who created the post.
        title (CharField): The title of the post (limited to 100 characters).
        game_link (URLField, optional): A link to a chess game related to the post (optional).
        body (TextField): The main content of the post.
        likes (ManyToManyField): likes of post.
        date_added (DateTimeField): The date and time when the post was created.
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    game_link = models.URLField(max_length=60, blank=True, null=True, validators=[validate_chess_game_url])
    body = models.TextField()
    likes = models.ManyToManyField(User, through="Like", related_name="liked_posts")

    def __str__(self) -> str:
        return f"User: {self.user} | Post: {self.title} | ID : {self.id}"