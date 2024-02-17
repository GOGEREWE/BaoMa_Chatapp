from django.urls import path
from . import views

urlpattern=[
    
    path('upload/',views.add_article),
    path('download/',views.load_art),

]
