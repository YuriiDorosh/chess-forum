from datetime import datetime

from django.test import TestCase
from room_messages.models import Message
from rooms.models import Room
from users.models.user import User


class MessageModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username="testuser",
            bio="Test bio",
            telegram_id="test123",
            chess_profile_url="https://example.com/testuser",
            subscriber=True,
        )

        self.room = Room.objects.create(name="Test Room", slug="test-room", premium=False)

        self.message = Message.objects.create(
            room=self.room, user=self.user, content="This is a test message.", date_added=datetime.now()
        )

    def test_message_creation(self):
        self.assertEqual(self.message.room, self.room)
        self.assertEqual(self.message.user, self.user)
        self.assertEqual(self.message.content, "This is a test message.")

    def test_auto_date_added(self):
        new_message = Message.objects.create(room=self.room, user=self.user, content="Another test message.")
        self.assertIsNotNone(new_message.date_added)
