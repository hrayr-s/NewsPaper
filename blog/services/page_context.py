import datetime

from blog.models import Article, Category
from blog.services.structures import Article as ArticleStruct
from django.db import models
from django.utils import timezone


def _get_next_featured_category(count=2):
    for category in Category.objects.annotate(
            count=models.Count(
                'articles',
                filter=models.Q(main_articles__published_at__gte=timezone.now() - datetime.timedelta(days=7)))
    ).order_by('-count')[:count]:
        yield category


def _get_featured_articles(*, count=2):
    for article in Article.objects.filter(
            featured=True
    ).select_related(
        'category'
    ).prefetch_related(
        'tags', 'categories'
    ).order_by('-featured_at', '-published_at')[:count]:
        yield ArticleStruct(
            id=article.id,
            title=article.title,
            description=article.description,
            content=article.content,
            published_at=article.published_at,
            slug=article.slug,
            author=article.author,
            tags=article.tags.all().values_list('name', flat=True),
            cover_image_url=article.image,
            category_name=article.category.name,
            related_categories_ids=article.categories.all().values_list('id', flat=True)
        )


def get_home_page_context(request):
    context = {}
    context.update({
        'featured_articles': _get_featured_articles(count=5)
    })

    # Main Post Details
    last_post = Article.objects.order_by('-published_at').first()
    context['last_post_title'] = last_post and last_post.title
    context['last_post_body'] = last_post and last_post.description
    context['last_post_image'] = last_post and last_post.image.url
    context['last_post_slug'] = last_post and last_post.slug

    # All news ordered by published time
    context['news_paper'] = Article.objects.all().exclude(
        id__in=[
            *(last_post and [last_post.id] or []),
            *[article.id for article in context['featured_articles']]
        ]
    )

    return context
