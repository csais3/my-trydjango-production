"""
To render html pages
"""
from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article
import random



def home_view(request):

    # generate a random number for the id
    random_id = random.randint(1,2)
    articles_list = Article.objects.all()
    my_list = articles_list
    article_obj = Article.objects.get(id=random_id)
    context = {
        'articles': my_list,
        'article': article_obj
    }
    return render(request, 'home_view.html', context)
