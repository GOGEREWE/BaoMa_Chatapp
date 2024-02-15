from uu import decode
from django.http.response import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, "chat_manage/index.html")


def room(request, room_name):
    return render(request, "chat_manage/chat_room.html", {"room_name": room_name})

def test(request):
    a1={"id":"1234","name": "小樱","age":30,"Tag": ["热爱羽毛球"],"child":[{"id":1,"sex":"小宝","age":5}],"location":"河南","introduction":"大家好，很期待和大家交流"}
    a2={"title":"world","concent":"456"}
    
    a=[]
    a.append(a1)
    a.append(a2)
    
    return JsonResponse(a1,safe=False)