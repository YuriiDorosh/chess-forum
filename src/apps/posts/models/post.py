from datetime import date

from core.models import BaseModel
from core.validators import validate_chess_game_url
from django.db import models
from django.utils import timezone
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFit
from users.models.user import User


def user_post_image_upload_path(instance, filename):
    today = date.today()
    return f'user_post_images/{today.year}/{today.month}/{today.day}/{timezone.now().strftime("%H-%M-%S")}_{filename}'


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
    game_link = models.URLField(
        max_length=60, blank=True, null=True, validators=[validate_chess_game_url]
    )
    body = models.TextField()
    likes = models.ManyToManyField(User, through="Like", related_name="liked_posts")

    def __str__(self) -> str:
        return f"User: {self.user} | Post: {self.title} | ID : {self.id}"


class UserPostImage(models.Model):
    """
    A model representing images associated with user posts.

    Attributes:
        post (ForeignKey): The post to which the image is attached.
        image (ProcessedImageField): The processed image file.
    """

    post = models.ForeignKey(UserPost, on_delete=models.CASCADE, related_name="image")
    image = ProcessedImageField(
        upload_to=user_post_image_upload_path,
        processors=[ResizeToFit(800, 800)],
        format="JPEG",
        options={"quality": 90},
        blank=True,
        null=True,
    )

    def __str__(self) -> str:
        return f"Added a photo to the post: {self.post} "
