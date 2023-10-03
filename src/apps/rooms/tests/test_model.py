from django.db import IntegrityError
from django.test import TestCase
from rooms.models.room import Room


class RoomModelTestCase(TestCase):
    def setUp(self):
        self.room = Room.objects.create(name="Test Room", slug="test-room")

    def test_room_creation(self):
        self.assertEqual(self.room.name, "Test Room")
        self.assertEqual(self.room.slug, "test-room")
        self.assertFalse(self.room.premium)

    def test_unique_slug_constraint(self):
        with self.assertRaises(IntegrityError):
            duplicate_room = Room(name="Duplicate Room", slug="test-room")
            duplicate_room.save()

    def test_premium_flag(self):
        premium_room = Room.objects.create(name="Premium Room", slug="premium-room", premium=True)
        self.assertTrue(premium_room.premium)
