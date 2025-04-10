import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
import board.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WhiteBoard.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            board.routing.websocket_urlpatterns
        )
    ),
})
