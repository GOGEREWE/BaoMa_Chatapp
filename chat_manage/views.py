import json
import queue

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render


USER_QUEUE = {}

def index(request):
    return render(request, "chat_manage/index.html")


def room(request, room_name):
    return render(request, "chat_manage/chat_room.html", {"room_name": room_name})

def home(request,uid):
    
    USER_QUEUE[uid] = queue.Queue()
    print(uid)
    print(USER_QUEUE)
    return HttpResponse("home sucess!!!")

def send(request,uid,room_name):
    text = request.GET.get('text')
    print(text)
    for uid,msg_list in USER_QUEUE.items():  #返回键、值
         
         msg_list.put(text)
         print(uid,msg_list)
    return HttpResponse("send sucess!!!")

def receive(request,uid,room_name):
    
    q = USER_QUEUE[uid]
    
    result = {'status': True,'data': None}
    try:
        data = q.get(timeout=2) #等待两秒
        result["data"] = data
    except queue.Empty as e:
        result['status'] = False
    return JsonResponse(result)
    
    





def test(request):
    a1={"id":"1234","name": "小樱","age":30,"Tag": ["热爱羽毛球"],"child":[{"id":1,"sex":"小宝","age":5}],"location":"河南","introduction":"大家好，很期待和大家交流"}
    #a2={"title":"world","concent":"456"}
    
   # a=[]
   # a.append(a1)
   # a.append(a2)
    
   # a3=json.dumps(a1)
    return JsonResponse(a1,safe=False)