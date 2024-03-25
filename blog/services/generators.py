import typing

from django.db.models import QuerySet
from django.utils.translation import get_language

from blog.models import Article, Category
from blog.services.structures import Article as ArticleStruct, Category as CategoryStruct


def article_struct_from_queryset(
        articles_qs: QuerySet[Article], lang: typing.Optional[str] = None
) -> typing.Generator[ArticleStruct, None, None]:
    lang = lang or get_language()
    for article in articles_qs:
        yield ArticleStruct.from_article_model(article=article, lang=lang)


def category_struct_from_queryset(
        categories_qs: QuerySet[Category], lang: typing.Optional[str] = None
) -> typing.Generator[CategoryStruct, None, None]:
    lang = lang or get_language()
    for category in categories_qs:
        yield CategoryStruct.from_category_model(category=category, lang=lang)
