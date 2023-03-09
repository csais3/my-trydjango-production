from django.urls import path
from .views import article_detail_view, articles_list_view, article_search_view, article_create_view

app_name = 'articles'

urlpatterns = [
    #path('', articles_list_view, name='articles_list'),
    path('<int:id>/', article_detail_view, name='article'),
    path('', article_search_view, name='search'),
    path('create/', article_create_view, name='create'),
]
