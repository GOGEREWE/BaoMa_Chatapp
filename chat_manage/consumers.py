# from channels import Group
# def ws_connect(message):
#     Group('users').add(message.reply_channel)
# def ws_disconnect(message):
#     Group('users').discard(message.reply_channel)

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
import json
import datetime


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = 'chat_%s' % self.room_name
        
        async_to_sync(self.cannel_layer.group_add)(self.room_name,self.room_group_name)
        self.accept()

    def websocket_receive(self, message):
        print("接收成功")
        message_json = json.loads(message)
        message_send = message_json['message']
        async_to_sync(self.channel_layer.group_send)(
            self.room_name,
            {
             'type': 'chat_message',
             'message': message
            })
    

    def chat_message(self, event):
        message = event['message']
        datetime_str = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        self.send(text_data=json.dump({
            
            'message':f'{datetime_str}:{message}'    
            
        }))


    def websocket_disconnect(self, close_code):
        print("断开连接")
        async_to_sync(self.channel_layer.group_discinnect)(self.room_name,self.room_group_name)
        raise StopConsumer()
    
