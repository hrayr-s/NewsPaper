from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.translation import get_language
from django.views.generic import ListView, DetailView

from blog.models import Article, Category
from blog.services.page_context import get_home_page_context
from blog.services.structures import Article as ArticleStruct

DEFAULT_ARTICLES_PER_PAGE = 10


class HomeView(ListView):
    template_name = 'blog/home.html'
    model = Article
    paginate_by = DEFAULT_ARTICLES_PER_PAGE

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = get_home_page_context(self.request)

        return context


class CategoryArticlesView(ListView):
    model = Article
    paginate_by = DEFAULT_ARTICLES_PER_PAGE
    template_name = 'blog/ArticleList.html'
    ordering = '-published_at'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        if self.kwargs['slug']:
            category = get_object_or_404(Category, slug=self.kwargs['slug'])
            object_list = self.get_queryset().filter(
                Q(category=category.id) | Q(categories__in=[category.id])).order_by(self.ordering)
            context['category_title'] = category.title
            context['category_image'] = category.image.url
            context['category_id'] = category.id

        context.update(super().get_context_data(object_list=object_list, **kwargs))

        return context


class UserArticlesView(ListView):
    model = Article
    paginate_by = DEFAULT_ARTICLES_PER_PAGE
    template_name = 'blog/ArticleList.html'
    ordering = '-published_at'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = {}
        creator = get_object_or_404(User, username=self.kwargs['username'])
        object_list = self.object_list.filter(
            creator=creator.id).order_by(self.ordering)
        context['category_title'] = 'Articles by ' + creator.username
        context['category_image'] = ''

        context.update(super().get_context_data(object_list=object_list, **kwargs))

        return context


class ArticleDetailView(DetailView):
    template_name = 'blog/ArticleDetail.html'
    model = Article

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return ArticleStruct.from_article_model(article=obj, lang=get_language())
