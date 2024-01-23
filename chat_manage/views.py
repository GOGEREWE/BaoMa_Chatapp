# coding=gbk
from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request,'chat_manage/index.html')

def room(request,room_name):
    return render(request,'chat_manage/room.html',{"room_name":room_name})