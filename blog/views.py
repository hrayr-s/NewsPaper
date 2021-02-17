from django.contrib.auth.models import User
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from blog.models import Article, Category

DEFAULT_ARTICLES_PER_PAGE = 10


class HomeView(ListView):
    template_name = 'blog/home.html'
    model = Article
    paginate_by = DEFAULT_ARTICLES_PER_PAGE

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = {}

        # Main Post Details
        last_post = Article.objects.order_by('-published_at')[0]
        context['last_post_title'] = last_post.title
        context['last_post_body'] = last_post.description
        context['last_post_image'] = last_post.image.url
        context['last_post_slug'] = last_post.slug

        f_categories = Category.objects.annotate(count=Count('article')).order_by('-count')

        # Featured category one
        f_category_1_post = Article.objects.filter(category=f_categories[0]).order_by('-published_at')[0]
        context['featured_one_category'] = f_category_1_post.category.title
        context['featured_one_title'] = f_category_1_post.title
        context['featured_one_body'] = f_category_1_post.description
        context['featured_one_image'] = f_category_1_post.image.url
        context['featured_one_slug'] = f_category_1_post.slug

        # Featured category one
        f_category_2_post = Article.objects.filter(category=f_categories[1]).order_by('-published_at')[0]
        context['featured_two_category'] = f_category_2_post.category.title
        context['featured_two_title'] = f_category_2_post.title
        context['featured_two_body'] = f_category_2_post.description
        context['featured_two_image'] = f_category_2_post.image.url
        context['featured_two_slug'] = f_category_2_post.slug

        # All news ordered by published time
        context['news_paper'] = Article.objects.all().exclude(id__in=[last_post.id, f_category_1_post.id,
                                                                      f_category_2_post.id])
        self.queryset = context['news_paper']
        context.update(super().get_context_data(object_list=context['news_paper'], **kwargs))

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
