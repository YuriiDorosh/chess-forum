from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views import View
from room_messages.models import Message
from rooms.services.room_service import RoomService


@method_decorator(login_required, name="dispatch")
class RoomView(View):
    """
    View for displaying a room's details.

    Attributes:
        None

    Methods:
        get(self, request, slug): Handles GET requests and renders the room details page.

    Template:
        room/room.html
    """

    def get(self, request, slug):
        """
        Handles GET requests and renders the room details page.

        Retrieves a room by its slug and retrieves the latest 25 messages for the room.

        Args:
            request (HttpRequest): The HTTP GET request object.
            slug (str): The slug of the room to display.

        Returns:
            HttpResponse: The rendered room details page.
        """
        room = RoomService.get_room_by_slug(slug)
        messages = Message.objects.filter(room=room)[0:25]
        return render(request, "room/room.html", {"room": room, "messages": messages})
