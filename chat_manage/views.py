from django.shortcuts import render


def index(request):
    return render(request, "chat_manage/index.html")


def room(request, room_name):
    return render(request, "chat_manage/chat_room.html", {"room_name": room_name})