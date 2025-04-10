import json
from channels.generic.websocket import AsyncWebsocketConsumer

class WhiteboardConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = f'whiteboard_{self.room_name}'
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def receive(self, text_data):
        data = json.loads(text_data)
        event_type = data.get('event')
        if event_type == "draw":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'draw_action',
                    'data': data
                }
            )
        elif event_type == "clear":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'clear_board',
                    'data': data
                }
            )
        elif event_type == "cursor":
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    'type': 'cursor_action',
                    'data': data
                }
            )

    async def cursor_action(self, event):
        # Send the cursor data to WebSocket clients
        await self.send(text_data=json.dumps(event['data']))


    async def clear_board(self, event):
        # Send a clear board message to clients
        await self.send(text_data=json.dumps(event['data']))


    async def draw_action(self, event):
        # Send the drawing data back to WebSocket clients
        await self.send(text_data=json.dumps(event['data']))
