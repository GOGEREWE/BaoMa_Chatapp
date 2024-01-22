from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'chat_manage/index.html',{})

def room(request):
    return render(request,'chat_manage/chat.html'{"room_name":room_name})