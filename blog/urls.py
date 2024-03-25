from django.urls import path

from blog.views import HomeView, CategoryArticlesView, ArticleDetailView, UserArticlesView

app_name = 'blog'

urlpatterns = [
    path('', HomeView.as_view()),
    path('category/<slug:slug>/', CategoryArticlesView.as_view(), name='CategoryArticlePage'),
    path('user/<slug:username>/', UserArticlesView.as_view(), name='UserArticlePage'),
    path('post/<slug:slug>/', ArticleDetailView.as_view(), name="ArticleDetailView")
]