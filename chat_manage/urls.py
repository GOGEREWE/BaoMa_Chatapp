from django.urls import include, path
from chat_manage import views

app_name="chat_manage"

urlpatterns = [ 
    
    path('<str:room_name>',views.room,name="room"),
    path('',views.index,name="index"),

]
