from django.shortcuts import render
from models import article
import json
# Create your views here.

def search_article(request):
    data_dict = json.loads(request)
    article = article.objects.f
