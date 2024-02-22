from django.http.response import JsonResponse
from django.shortcuts import render
from models import article,user
from django.db.models import Q
import json
# Create your views here.

def search_article(request):
    
    # table1.objects.filter(id__lt=10,id__gt=1)#��ȡidС��10,�Ҵ���1�ļ�¼
    # table1.objects.filter(id__in=[11,22,33,44])#��ȡid��[11,22,33,44]�еļ�¼
    # table1.objects.exclude(id__in=[11,22,33,44])#��ȡid����[11,22,33,44]�еļ�¼
    # table1.objects.filter(name__contains="content1")#��ȡname�а�����"contents"�ļ�¼(���ִ�Сд)
    # table1.objects.filter(name__icontains="content1")#��ȡname�а�����"content1"�ļ�¼(�����ִ�Сд)
 
    # table1.objects.filter(id__range=[1,4])#��ȡid��1��4(������4)֮��ĵļ�¼

    data_dict = json.loads(request)
    key = data_dict["key"]
    #����һ����������ؼ��ֵ���������
    articles = article.objects.filter(title__icontains=key)
    
    return JsonResponse(articles,safe=True)

def search_article(request):


    data_dict = json.loads(request)
    key = data_dict["id"]
    #����һ����������ؼ��ֵ���������
    users = user.objects.get(id = key)
    return JsonResponse(users,safe=True)