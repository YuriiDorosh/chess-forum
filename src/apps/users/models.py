import uuid

from django.contrib.auth.models import AbstractUser
from django.db import models
from users.validators import validate_chess_profile_url

class User(AbstractUser):
    """
    Custom User model that overrides the default Django User model.

    Fields:
    - username: User`s name (unique field).
    - bio: User's biography (optional field).
    - photo: User's photo (stored in the 'user_photos/' folder) (optional field).
    - telegram_id: Telegram ID (optional field).
    - chess_profile_url: URL to the user's chess profile (optional field).
    - subscriber: Whether the user is a subscriber (default is False).
    """

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(max_length=30, unique=True)
    bio = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="user_photos/", blank=True, null=True)
    telegram_id = models.CharField(max_length=30, blank=True, null=True)
    chess_profile_url = models.URLField(max_length=60, blank=True, null=True, validators=[validate_chess_profile_url])
    subscriber = models.BooleanField(default=False)
