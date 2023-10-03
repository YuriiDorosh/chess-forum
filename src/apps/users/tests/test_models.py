from django.db import IntegrityError
from django.test import TestCase

from apps.users.models.user import User


class UserModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            bio="Test bio",
            telegram_id="test123",
            chess_profile_url="https://example.com/testuser",
            subscriber=True,
        )

    def test_user_creation(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.bio, "Test bio")
        self.assertEqual(self.user.telegram_id, "test123")
        self.assertEqual(self.user.chess_profile_url, "https://example.com/testuser")
        self.assertTrue(self.user.subscriber)

    def test_default_subscriber_value(self):
        new_user = User.objects.create(username="newuser")
        self.assertFalse(new_user.subscriber)

    def test_unique_username_constraint(self):
        with self.assertRaises(IntegrityError):
            duplicate_user = User(
                username="testuser",
                bio="Duplicate user",
                telegram_id="test456",
                chess_profile_url="https://example.com/duplicateuser",
                subscriber=False,
            )
            duplicate_user.save()
