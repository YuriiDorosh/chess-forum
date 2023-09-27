from django.urls import path

from rooms.consumers import ChatConsumer

websocket_urlpatterns = [
    path('ws/<str:room_name>/', ChatConsumer.as_asgi()),
    # path('<str:room_name>/', ChatConsumer.as_asgi()),
]

