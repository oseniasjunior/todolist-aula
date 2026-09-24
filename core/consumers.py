from channels.generic.websocket import AsyncJsonWebsocketConsumer


class Consumer(AsyncJsonWebsocketConsumer):

    async def connect(self):
        print('Conectado ao canal')
        await self.accept()
        await self.channel_layer.group_add('test', self.channel_name)

    async def disconnect(self, close_code):
        print('Desconectado do canal')
        await self.channel_layer.group_discard('test', self.channel_name)

    async def group_message(self, event: dict):
        print(event)
        await self.send_json(event['content'])

    def receive_json(self, content, **kwargs):
        pass