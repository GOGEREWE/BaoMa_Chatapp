import json
import queue

from django.http import HttpResponse
from django.http.response import JsonResponse
from django.shortcuts import render

ROOM_QUEUE = {}

#def index(request):
#    return render(request, "chat_manage/index.html")

#def room(request, room_name):
#    return render(request, "chat_manage/chat_room.html", {"room_name": room_name})
"""
根据接受的双方id编号,根据既定房间命名规则确定聊天室,创建双方的信息接受队列进行数据接受

"""



def home(request):
    USER_QUEUE = {}
    my_id = request.GET.get('my_id')
    o_id = request.GET.get('o_id')
    if my_id > o_id:
        room_name = o_id + "&" + my_id
    else:
        room_name = my_id + "&" +o_id


    USER_QUEUE[my_id] = queue.Queue()
    USER_QUEUE[o_id] = queue.Queue()
    ROOM_QUEUE[room_name] = USER_QUEUE

    print(USER_QUEUE)
    return JsonResponse(room_name)

def send(request):
    room_name = request.GET.get('room_name')
    content = request.GET.get('content')
    print(content)
    for uid,msg_list in ROOM_QUEUE[room_name].items():  #返回键、值
         msg_list.put(content)
         print(uid,msg_list)
    return HttpResponse("send sucess!!!")



def receive(request):
    room_name = request.GET.get('room_name')
    uid = request.GET.get('my_id')
    q = ROOM_QUEUE[room_name][uid]
    result = {'status': True,'data': None}
    try:
        data = q.get(timeout=2) #等待两秒
        result["data"] = data
    except queue.Empty as e:
        result['status'] = False
        print(result)
    return JsonResponse(result)




"""
def test(request):
    a1={"id":"1234","name": "小樱","age":30,"Tag": ["热爱羽毛球"],"child":[{"id":1,"sex":"小宝","age":5}],"location":"河南","introduction":"大家好，很期待和大家交流"}
    #a2={"title":"world","concent":"456"}
    
    # a=[]
    # a.append(a1)
    # a.append(a2)
    
    # a3=json.dumps(a1)
    return JsonResponse(a1,safe=False)
"""