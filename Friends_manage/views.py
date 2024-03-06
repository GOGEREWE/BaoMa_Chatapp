from models import users
from django.http.response import JsonResponse
# Create your views here.



def add_friend(request):
    uid = request.GET.get('my_id')
    friend_id = request.GET.get('friend_id')
    result = True
    try:
        user = users.objects.get(id = uid)
        friend = users.objects.get(id = friend_id)
        user.frineds.add(friend)
        user.save()
    except:
        result = False
    return JsonResponse(result)

def remove_friend(request):
    uid = request.GET.get('my_id')
    friend_id = request.GET.get('friend_id')
    result =True
    try:
        friend = users.objects.get(id = friend_id)
        user = users.objects.get(id = uid)
        user.frends.remove(friend)
        user.save()
    except:
        result = False
    return JsonResponse(result)