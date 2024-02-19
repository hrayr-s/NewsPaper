import datetime

from blog.models import Article, Category
from django.db import models
from django.utils import timezone


def _get_next_featured_category(count=2):
    for category in Category.objects.annotate(
            count=models.Count(
                'articles',
                filter=models.Q(main_articles__published_at__gte=timezone.now() - datetime.timedelta(days=7)))
    ).order_by('-count')[:2]:
        yield category


def get_home_page_context(request):
    context = {}

    # Main Post Details
    last_post = Article.objects.order_by('-published_at').first()
    context['last_post_title'] = last_post and last_post.title
    context['last_post_body'] = last_post and last_post.description
    context['last_post_image'] = last_post and last_post.image.url
    context['last_post_slug'] = last_post and last_post.slug

    f_categories = _get_next_featured_category()

    # Featured category one
    f_category_1_post = Article.objects.filter(category=next(f_categories)).order_by('-published_at')[0]
    context['featured_one_category'] = f_category_1_post.category.title
    context['featured_one_title'] = f_category_1_post.title
    context['featured_one_body'] = f_category_1_post.description
    context['featured_one_image'] = f_category_1_post.image.url
    context['featured_one_slug'] = f_category_1_post.slug

    # Featured category two
    f_category_2_post = Article.objects.filter(category=next(f_categories)).order_by('-published_at')[0]
    context['featured_two_category'] = f_category_2_post.category.title
    context['featured_two_title'] = f_category_2_post.title
    context['featured_two_body'] = f_category_2_post.description
    context['featured_two_image'] = f_category_2_post.image.url
    context['featured_two_slug'] = f_category_2_post.slug

    # All news ordered by published time
    context['news_paper'] = Article.objects.all().exclude(id__in=[last_post.id, f_category_1_post.id,
                                                                  f_category_2_post.id])

    return context
