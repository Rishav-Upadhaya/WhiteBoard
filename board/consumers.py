import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.exceptions import StopConsumer

# This file defines the WebSocket consumer for the whiteboard application.
# It handles WebSocket connections, processes incoming messages, and broadcasts events to all users in the same room.

class WhiteboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        try:
            # Extract the room name from the WebSocket URL and create a group name for the room.
            # Add the WebSocket connection to the group and accept the connection.
            self.room_name = self.scope['url_route']['kwargs']['room_name']
            self.room_group_name = f'whiteboard_{self.room_name}'
            
            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
            await self.accept()
        except Exception as e:
            print(f"Connection error: {e}")
            raise StopConsumer()

    async def disconnect(self, close_code):
        # Remove the connection from the room group when disconnecting
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        try:
            # Handle incoming WebSocket messages.
            # Depending on the event type, broadcast the message to all users in the room.
            data = json.loads(text_data)
            event_type = data.get('event')
            if event_type == "draw":
                # Broadcast drawing actions to all users in the room.
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'draw_action',
                        'data': data
                    }
                )
            elif event_type == "clear":
                # Broadcast a clear board action to all users in the room.
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'clear_board',
                        'data': data
                    }
                )
            elif event_type == "cursor":
                # Broadcast cursor movement actions to all users in the room.
                await self.channel_layer.group_send(
                    self.room_group_name,
                    {
                        'type': 'cursor_action',
                        'data': data
                    }
                )
        except Exception as e:
            print(f"Error processing message: {e}")
            await self.send(text_data=json.dumps({
                'error': 'Failed to process message'
            }))

    async def cursor_action(self, event):
        # Send cursor movement data to WebSocket clients.
        await self.send(text_data=json.dumps(event['data']))

    async def clear_board(self, event):
        # Send a clear board message to WebSocket clients.
        await self.send(text_data=json.dumps(event['data']))

    async def draw_action(self, event):
        # Send drawing data to WebSocket clients.
        await self.send(text_data=json.dumps(event['data']))
