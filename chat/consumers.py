from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        print('connected: %s' % self.scope['user'])
        self.accept()

    def disconnect(self, close_code):
        print('disconnected')

    def receive(self, text_data):
        print('receive: %s' % text_data)
        self.send('The data is %s received at the server side!' % text_data)

    def chat_message(self, event):
        pass
