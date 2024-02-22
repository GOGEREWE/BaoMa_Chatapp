import json
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from models import user,article
from math import sin, cos, sqrt, atan2, radians,degrees
# Create your views here.

# class user:
#     def __init__(self):
#         self.id=""
#         self.tag=""
#         self.lon_lat=[]
class candidate:
    def __int__(self):
        self.id=""         #�û�ID
        self.name=""       #�û���
        self.inclusion=""  #�û��Ƽ�ֵ
        self.distance=""   #�û�����
        #other...

#�����û���Ϣ����ɺ����Ƽ����ܣ�ͨ��Http����json��ʽ���Ƽ��û���Ϣ
#ģ���Ƽ�����
def friend_referral(request,user_id): 
    data_dict = json.loads(request)
    #user_id = data_dict.id

    ch_tag = data_dict.tag  #�����ǩ
    _age = data_dict.age    #ĸ�����䷶Χ
    work_status = data_dict.work_satus   #����״̬
    dist = data_dict.distance #���뷶Χ
    this_user = user.objects.get(id=user_id)
    can_user=[]
    
    min_lat, max_lat, min_lon, max_lon = calculate_bounding_box(this_user.lat,this_user.lon,dist)
    condition = Q(lat__gte=min_lat)&Q(lat__lte=max_lat)&Q(lon__gte=min_lon)&Q(lon__lte=max_lon)&Q(age__gte=_age[0][0])&Q(age__lte=_age[0][1])&Q(child__gte=_age[1][0])&Q(child__lte=_age[1][1])
    users = user.objects.filter(condition)
    # condition = Q(age__gte=_age[0][0])&Q(age__lte=_age[0][1])&Q(child__gte=_age[1][0])&Q(child__lte=_age[1][1])
    

        # if len(can_user) < 10:
        #     users = user.objects.order_by('?')[:10]
    for users_count in users:
        inclusion = count_duplicate_characters(ch_tag,users_count.tag)/len(users_count.tag)
        if inclusion > 1 and not users_count.id in this_user.item:
            candidate.distance = calculate_distance(this_user.lon_lat[0],this_user.lon_lat[1],users_count.lon_lat[0],users_count.lon_lat[1])
            candidate.id = users_count.id
            candidate.inclusion = inclusion
                
            can_user.append(candidate())
        
    json_candidate = json.dumps(can_user)
    return JsonResponse(json_candidate,content_type='application/json')

#�����Ƽ����ܣ����ݱ�ǩ���ƶȣ�Ϊ�û��Ƽ��������û���Ȥ��Χ�ڵ���������
def rec_articel(request,user_id):
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

#�����ǩ���ƶ�
def count_duplicate_characters(str1, str2):
    set1 = set(str1)
    set2 = set(str2)
    common_chars = set1.intersection(set2)
    return len(common_chars)

#���ݾ�γ�ȼ���ֱ�߾���
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

def calculate_bounding_box(center_lat, center_lon, distance):
    # ����뾶����λ������
    radius = 6371

    # �����ĵ�ľ�γ��ת��Ϊ����
    center_lat_rad = radians(center_lat)
    center_lon_rad = radians(center_lon)

    # ����γ�ȵķ�Χ
    lat_diff = distance / radius
    min_lat = degrees(center_lat_rad - lat_diff)
    max_lat = degrees(center_lat_rad + lat_diff)

    # ���㾭�ȵķ�Χ
    lon_diff = distance / (radius * cos(center_lat_rad))
    min_lon = degrees(center_lon_rad - lon_diff)
    max_lon = degrees(center_lon_rad + lon_diff)

    return min_lat, max_lat, min_lon, max_lon