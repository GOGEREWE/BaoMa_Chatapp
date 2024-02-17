# chat/urls.py
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    
    path("<str:uid>/",views.home,name = "home"),
    
    path("<str:uid>/<str:room_name>/send",views.send,name = "send"),
    
    path("<str:uid>/<str:room_name>/receive",views.receive,name = "receive"),
    
    #path("<str:room_name>/", views.room, name="room"),
    #path("test/",views.test),
]
