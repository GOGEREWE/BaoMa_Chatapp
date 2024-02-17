import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from models import user,article
from math import sin, cos, sqrt, atan2, radians
# Create your views here.

# class user:
#     def __init__(self):
#         self.id=""
#         self.tag=""
#         self.lon_lat=[]
class candidate:
    def __int__(self):
        self.id=""         #用户ID
        self.name=""       #用户名
        self.inclusion=""  #用户推荐值
        self.distance=""   #用户距离
        #other...

#处理用户信息，完成好友推荐功能，通过Http返回json格式的推荐用户信息
def friend_referral(request):
    data_dict = json.loads(request)
    user_id = data_dict.id
    can_user=[]
    user = user.objects.get(id=user_id)

    if len(can_user) < 10:
        users = user.objects.order_by('?')[:10]
        for users_count in users:
            i = 0
            inclusion = count_duplicate_characters(user.tag,users_count.tag)/len(users_count.tag)
            if inclusion > 0.5 and not users_count.id in user.item:
                candidate.distance = calculate_distance(user.lon_lat[0],user.lon_lat[1],users_count.lon_lat[0],users_count.lon_lat[1])
                candidate.id = users_count.id
                candidate.inclusion = inclusion
                
                can_user.append(candidate())
        
    json_candidate = json.dumps(can_user)
    return JsonResponse(json_candidate,content_type='application/json')


def rec_articel(request):
    can_articel=[]
    user = request.user

    if len(can_articel) < 10:
        articles = article.objects.order_by('?')[:10]
        for article_count in articles:
            i = 0
            inclusion = count_duplicate_characters(user.tag,article_count.tag)/len(user.tag)
            if inclusion > 0.5 and not article_count.id in user.item:
                candidate.id = article_count.id
                candidate.inclusion = inclusion
                can_articel.append(candidate())
        
    json_articel = json.dumps(can_articel)
    return JsonResponse(json_articel,content_type='application/json')

#计算标签相似度
def count_duplicate_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common_chars = set1.intersection(set2)
    return len(common_chars)

#根据经纬度计算直线距离
def calculate_distance(lat1, lon1, lat2, lon2):
    R = 6371.0
    lat1_rad = radians(lat1)
    lon1_rad = radians(lon1)
    lat2_rad = radians(lat2)
    lon2_rad = radians(lon2)
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad
    a = sin(dlat / 2)**2 + cos(lat1_rad) * cos(lat2_rad) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance