
from django.contrib import admin
from django.urls import path, include
from .views import home_view

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', home_view, name='index'),
    path('articles/', include('articles.urls')),
    path('accounts/', include('accounts.urls')),
]
