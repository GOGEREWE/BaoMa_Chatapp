from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from models import user
# Create your views here.


#��Ӻ���
def add_friend(request,user_id):
    user = request.user
    friend = user.objects.get(id = user_id)
    user.frineds.add(friend)
    user.save()
    return HttpResponseRedirect(reverse('profile')) #�ض��򷵻���������Ϣҳ��

#ɾ������
def remove_friend(request,user_id):
    user = request.user
    friend = user.objects.get(id = user_id)
    user.frends.remove(friend)
    user.save()
    return HttpResponseRedirect(reverse('friends_list')) #�ض��򷵻ص������б�
    