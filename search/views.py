from django.http.response import JsonResponse
from django.shortcuts import render
from models import article,user
from django.db.models import Q
import json
# Create your views here.

def search_article(request):
    
    # table1.objects.filter(id__lt=10,id__gt=1)#获取id小于10,且大于1的记录
    # table1.objects.filter(id__in=[11,22,33,44])#获取id在[11,22,33,44]中的记录
    # table1.objects.exclude(id__in=[11,22,33,44])#获取id不在[11,22,33,44]中的记录
    # table1.objects.filter(name__contains="content1")#获取name中包含有"contents"的记录(区分大小写)
    # table1.objects.filter(name__icontains="content1")#获取name中包含有"content1"的记录(不区分大小写)
 
    # table1.objects.filter(id__range=[1,4])#获取id在1到4(不包含4)之间的的记录

    data_dict = json.loads(request)
    key = data_dict["key"]
    #返回一个标题包含关键字的文章数据
    articles = article.objects.filter(title__icontains=key)
    
    return JsonResponse(articles,safe=True)

def search_article(request):


    data_dict = json.loads(request)
    key = data_dict["id"]
    #返回一个标题包含关键字的文章数据
    users = user.objects.get(id = key)
    return JsonResponse(users,safe=True)