from django.urls import path
from rooms.views.all_rooms_views import AllRoomsView
from rooms.views.room_views import RoomView

app_name = "rooms"

urlpatterns = [
    path("", AllRoomsView.as_view(), name="rooms"),
    path("<slug:slug>/", RoomView.as_view(), name="room"),
]
