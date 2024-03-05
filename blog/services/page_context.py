import datetime

from django.db import models
from django.utils import timezone
from django.utils.translation import get_language

from blog.models import Article, Category
from blog.services.structures import Article as ArticleStruct


def _get_next_featured_category(count=2):
    for category in Category.objects.annotate(
            count=models.Count(
                'articles',
                filter=models.Q(main_articles__published_at__gte=timezone.now() - datetime.timedelta(days=7)))
    ).order_by('-count')[:count]:
        yield category


def _get_featured_articles(*, count=2):
    lang = get_language()
    for article in Article.objects.filter(
            featured=True
    ).select_related(
        'category'
    ).prefetch_related(
        'content', 'content__tags', 'categories', 'category__content'
    ).order_by('-featured_at', '-published_at')[:count]:
        yield ArticleStruct.from_article_model(article=article, lang=lang)


def get_home_page_context(request):
    context = {}
    context.update({
        'featured_articles': _get_featured_articles(count=5)
    })

    # Main Post Details
    last_post = Article.objects.order_by('-published_at').first()
    last_post_content = last_post and last_post.content.filter(language=get_language()).first()
    context['last_post_title'] = last_post and last_post_content.title
    context['last_post_body'] = last_post and last_post_content.description
    context['last_post_image'] = (
            last_post and last_post_content.image and last_post_content.image.url
            or last_post and last_post.image.url
    )
    context['last_post_slug'] = last_post and last_post.slug

    # All news ordered by published time
    context['news_paper'] = Article.objects.all().exclude(
        id__in=[
            *(last_post and [last_post.id] or []),
            *[article.id for article in context['featured_articles']]
        ]
    )

    return context
