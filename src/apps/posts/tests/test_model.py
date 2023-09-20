from django.test import TestCase
from users.models import User
from posts.models import UserPost
from datetime import datetime


class UserPostModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            bio="Test bio",
            telegram_id="test123",
            chess_profile_url="https://example.com/testuser",
            subscriber=True,
        )

        self.post = UserPost.objects.create(
            user=self.user,
            title="Test Post",
            game_link="https://example.com/game123",
            body="This is a test post.",
            date_added=datetime.now(),
        )

    def test_user_post_creation(self):
        self.assertEqual(self.post.user, self.user)
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.game_link, "https://example.com/game123")
        self.assertEqual(self.post.body, "This is a test post.")

    def test_default_date_added(self):
        new_post = UserPost.objects.create(user=self.user, title="Another Test Post", body="This is another test post.")
        self.assertIsNotNone(new_post.date_added)

    def test_optional_game_link(self):
        post_without_game_link = UserPost.objects.create(
            user=self.user, title="Post Without Game Link", body="This post has no game link."
        )
        self.assertIsNone(post_without_game_link.game_link)
