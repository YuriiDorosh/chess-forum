from django.db import models
from core.models import BaseModel
from users.models.user import User
from posts.models.post import UserPost

class Like(BaseModel):
    """
    A model representing user likes on the posts.

    Attributes:
        user (ForeignKey): The user who liked the post.
        post (ForeignKey): The post that was liked by the user.
        date_added (DateTimeField): The date and time when the post was created.
    """
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)

    class Meta:
        unique_together = ["user", "post"]

    def __str__(self) -> str:
        return f"Who liked: {self.user} | Post Creator: {self.post.user} | Post: {self.post.title}"