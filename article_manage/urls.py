from django.urls import path
from . import views

urlpattern=[
    path('/load',views.load_art)
]
