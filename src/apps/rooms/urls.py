from django.urls import path

from rooms.views import rooms, room

app_name = "rooms"

urlpatterns = [
    path("", rooms, name="rooms"),
    path("<slug:slug>/", room, name="room"),
]
