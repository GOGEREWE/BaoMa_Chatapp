from django.http.response import JsonResponse
from django.shortcuts import render


def index(request):
    return render(request, "chat_manage/index.html")


def room(request, room_name):
    return render(request, "chat_manage/chat_room.html", {"room_name": room_name})

def test(request):
    a1={"title":"hello","concent":"123"}
    a2={"title":"world","concent":"456"}
    
    a=[]
    a.append(a1)
    a.append(a2)
    return JsonResponse(a,safe=False)