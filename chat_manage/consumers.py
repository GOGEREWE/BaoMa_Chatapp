# from channels import Group


# def ws_connect(message):
#     Group('users').add(message.reply_channel)
    
# def ws_disconnect(message):
#     Group('users').discard(message.reply_channel)
from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer

class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        return self.accept()
    
    def websocket_receive(self, message):
        print("发送成功")
        return self.send()

    def websocket_disconnect(self, message):
        print("断开连接")
        raise StopConsumer()
    
