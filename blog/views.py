from django.db.models import Q
from django.shortcuts import get_object_or_404
from django.utils.translation import get_language
from django.views.generic import ListView, DetailView

from accounts.models import User
from blog.models import Article, Category
from blog.services.generators import article_struct_from_queryset
from blog.services.page_context import get_home_page_context
from blog.services.structures import Article as ArticleStruct, Category as CategoryStruct, Page

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
    category = None

    def get_queryset(self):
        if not self.category:
            return super().get_queryset()

        return super().get_queryset().filter(
            Q(category=self.category.id) | Q(categories__in=[self.category.id])).order_by(self.ordering)

    def get_context_data(self, *, object_list=None, **kwargs):
        if slug := self.kwargs.get('slug', None):
            category = get_object_or_404(Category, slug=slug)
            self.category = CategoryStruct.from_category_model(category=category)

        context = super().get_context_data(object_list=object_list, page=self.category, **kwargs)

        context['page_obj'] = context['page_obj'] and article_struct_from_queryset(context['page_obj'])
        context['object_list'] = context['object_list'] and article_struct_from_queryset(context['object_list'])

        return context


class UserArticlesView(CategoryArticlesView):
    model = Article
    paginate_by = DEFAULT_ARTICLES_PER_PAGE
    template_name = 'blog/AuthorArticleList.html'
    ordering = '-published_at'
    author = None

    def get_queryset(self):
        if not self.author:
            return super().get_queryset()

        return super().get_queryset().filter(author=self.author.id)

    def get_context_data(self, *, object_list=None, **kwargs):
        self.author = get_object_or_404(User, username=self.kwargs['username'])
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['page'] = Page.from_user_obj(user=self.author)
        return context


class ArticleDetailView(DetailView):
    template_name = 'blog/ArticleDetail.html'
    model = Article

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        return ArticleStruct.from_article_model(article=obj, lang=get_language())
