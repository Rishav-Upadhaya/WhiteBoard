from django.urls import re_path
from . import consumers

# This file defines the WebSocket routing for the whiteboard application.
# It maps WebSocket URL patterns to their corresponding WebSocket consumers.

websocket_urlpatterns = [
    re_path(r'ws/whiteboard/(?P<room_name>\w+)/$', consumers.WhiteboardConsumer.as_asgi()),
    # The above pattern captures the room name from the WebSocket URL and routes it to the WhiteboardConsumer.
]
