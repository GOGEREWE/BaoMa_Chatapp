from django.urls import include, path
from views import *

app_name="chat_manage"

urlpatterns = [ 
    
    path('chat/',room,name="chat"),
    path('',index,name="index"),

]
