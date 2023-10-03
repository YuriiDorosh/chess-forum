import os
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.dev")

django_application = get_asgi_application()

from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from apps.rooms import routing

application = ProtocolTypeRouter(
    {"http": django_application, "websocket": AuthMiddlewareStack(URLRouter(routing.websocket_urlpatterns))}
)
