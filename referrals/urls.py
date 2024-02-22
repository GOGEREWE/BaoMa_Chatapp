from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
path("/friend/<str:user_id>/",views.friend_referral,name="friend_referral"),

path("/articel/<str:user_id>/",views.rec_articel,name="friend_referral"),

]