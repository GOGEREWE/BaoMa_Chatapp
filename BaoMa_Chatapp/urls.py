# mysite/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("chat/", include("chat_manage.urls")),
    #path("referrals/",include("Friend_referrals")),
    path("admin/", admin.site.urls),
]