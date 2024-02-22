from urllib.parse import urlparse
from django.urls import path
from . import views

urlpatterns = [
    path("user/",views.search),
    path("article/",views.search),
    path("address/",views.search),

]
