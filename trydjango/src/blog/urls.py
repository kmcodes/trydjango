from django.urls import path
from .views import (
        
        ArticleListView,
        ArticleDetailView
    )



app_name = 'blog'

urlpatterns = [

    path('<int:id>/',ArticleDetailView.as_view(), name='article-detail'),
    path('list/',ArticleListView.as_view(),name='article-list'),

]