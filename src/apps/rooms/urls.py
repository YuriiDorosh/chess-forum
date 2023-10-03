from django.urls import path
from rooms.views import room, rooms

app_name = "rooms"

urlpatterns = [
    path("", rooms, name="rooms"),
    path("<slug:slug>/", room, name="room"),
]
