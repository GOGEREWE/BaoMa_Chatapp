from django.http.response import JsonResponse
from django.shortcuts import render
from models import article
from django.db.models import Q
# Create your views here.

def search_article(request):
    q = request.GET.get('q')
    tag = request.GET.get('tag')
    error_msg = ''
    result = {'error_msg':error_msg}
    if not q:
        error_msg = "请输入关键词"
        return JsonResponse(result)
    articles = article.objects.filter(Q(title__icontains=q)|Q(content__icontains=q))
    for this_tag in tag:
        condition = condition & Q(tag__icontain=this_tag)

    article_list = articles.objects.filter(condition)
    result['article_list'] = article_list
    return JsonResponse(articles,safe=True)

def search_article(request):
    q = request.GET.get('q')
    error_msg = ''
    result = {'error_msg':error_msg}
    if not q:
        error_msg = "请输入关键词"
        return JsonResponse(result)
    article_list = article.objects.filter(Q(title__icontains=q)|Q(content__icontains=q))
    result['article_list']=article_list
    return JsonResponse(result)


    # table1.objects.filter(id__lt=10,id__gt=1)#��ȡidС��10,�Ҵ���1�ļ�¼
    # table1.objects.filter(id__in=[11,22,33,44])#��ȡid��[11,22,33,44]�еļ�¼
    # table1.objects.exclude(id__in=[11,22,33,44])#��ȡid����[11,22,33,44]�еļ�¼
    # table1.objects.filter(name__contains="content1")#��ȡname�а�����"contents"�ļ�¼(���ִ�Сд)
    # table1.objects.filter(name__icontains="content1")#��ȡname�а�����"content1"�ļ�¼(�����ִ�Сд)
    # table1.objects.filter(id__range=[1,4])#��ȡid��1��4(������4)֮��ĵļ�¼