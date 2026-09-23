from channels.generic.websocket import AsyncJsonWebsocketConsumer


class Consume(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print('Conectado ao canal')
        await self.connect()
        await self.channel_layer.group_add('test', self.channel_name)

    async def disconnect(self, close_code):
        print('Desconectado do canal')
        await self.disconnect()
        await self.channel_layer.group_discard('test', self.channel_name)

    async def group_message(self, event):
        await self.send_json(event['message'])

    def receive_json(self, content, **kwargs):
        pass