from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from models import user
# Create your views here.


#添加好友
def add_friend(request,user_id):
    user = request.user
    friend = user.objects.get(id = user_id)
    user.frineds.add(friend)
    user.save()
    return HttpResponseRedirect(reverse('profile')) #重定向返回至个人信息页面

#删除好友
def remove_friend(request,user_id):
    user = request.user
    friend = user.objects.get(id = user_id)
    user.frends.remove(friend)
    user.save()
    return HttpResponseRedirect(reverse('friends_list')) #重定向返回到好友列表
    