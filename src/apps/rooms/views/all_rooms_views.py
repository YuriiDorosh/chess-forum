from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from rooms.services.room_service import RoomService


@method_decorator(login_required, name="dispatch")
class AllRoomsView(View):
    """
    View for displaying a list of all available rooms.

    Attributes:
        None

    Methods:
        get(self, request): Handles GET requests and renders the list of rooms.

    Template:
        room/rooms.html
    """

    def get(self, request):
        """
        Handles GET requests and renders the list of all available rooms.

        Retrieves a list of all rooms using the RoomService.

        Args:
            request (HttpRequest): The HTTP GET request object.

        Returns:
            HttpResponse: The rendered list of rooms.
        """
        rooms = RoomService.get_all_rooms()
        return render(request, "room/rooms.html", {"rooms": rooms})
