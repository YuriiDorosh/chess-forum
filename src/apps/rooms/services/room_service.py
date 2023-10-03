from rooms.models.room import Room

class RoomService:
    @staticmethod
    def get_all_rooms():
        """
        Retrieves all rooms from the database.

        Returns:
            QuerySet: A query containing all rooms.
        """
        return Room.objects.all()

    @staticmethod
    def get_room_by_slug(some_slug):
        """
        Retrieves a room from the database by its slug.

        Args:
            some_slug (str): The slug of the room to retrieve.

        Returns:
            Room: The room with the specified slug.
        """
        return Room.objects.get(slug=some_slug)
