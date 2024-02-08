from django.urls import path
from . import views

path("<str:user_id>/",views.friend_referral,name="friend_referral")
