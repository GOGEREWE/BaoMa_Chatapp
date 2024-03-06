from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from models import user

# Create your views here.


def modify(request,change):
    
    change_user = request.user
    
    user = user.objects.get(id = change_user.id)
    user.name = change.name
    user.age = change.age
    user.tag = change.tag
    
    user.save()
    return HttpResponseRedirect(reverse('profile'))

def log_off(request,user_id):
    user = user.objects.get(id = user_id).delete()
    return HttpResponseRedirect(reverse('index'))

def add_tag(request,tag_id):
    user = request.user
    user.tag = user.tag + tag_id
    user.save()
    return HttpResponseRedirect(reverse('tag_page'))

def rm_tag(request,tag_id):
    user = request.user
    user.tag.replace(tag_id,'')
    user.save()
    