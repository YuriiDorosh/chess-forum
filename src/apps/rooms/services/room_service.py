from rooms.models.room import Room


class RoomService:
    @staticmethod
    def get_all_rooms():
        return Room.objects.all()

    @staticmethod
    def get_room_by_slug(some_slug):
        return Room.objects.get(slug=some_slug)
