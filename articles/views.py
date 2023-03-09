from django.shortcuts import render
from .models import Article

from .forms import ArticleForm
from django.contrib.auth.decorators import login_required

# Create your views here.



def article_search_view(request):
    query_dict = request.GET # This is a dictionary
    try:
        query = int(query_dict.get('q'))
    except:
        query = None
    article_object = None
    if query is not None:
        article_object = Article.objects.get(id=query)
    context = {
        'article': article_object
    }
    return render(request, 'articles/search.html', context)

def articles_list_view(request):
    articles = Article.objects.all()
    context = {
        'articles': articles
    }
    return render(request, 'articles/home_view.html', context)

def article_detail_view(request, id=None):
    article = None
    if id is not None:
        article= Article.objects.get(id=id)
        context = {
            'article': article
        }

    return render(request, 'articles/article_detail_view.html', context)

@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        article_object = form.save()
        context['form'] = ArticleForm()
    return render(request, 'articles/create.html', context)