import dataclasses
import datetime
import typing
from typing import List

from django.db.models import QuerySet
from django.utils.translation import get_language

from blog.models import Article as ArticleModel, Category as CategoryModel


@dataclasses.dataclass
class Category(object):
    title: str
    slug: str
    lang: str
    image: typing.Optional[str] = None

    @classmethod
    def from_category_model(cls, *, category: CategoryModel, lang: typing.Optional[str] = None) -> 'Category':
        lang = lang or get_language()
        content = list(content for content in category.content.all() if content.language == lang)[0]
        return Category(
            title=content.title,
            slug=category.slug,
            lang=lang,
            image=category.image.url
        )


@dataclasses.dataclass
class Article(object):
    id: int
    title: str
    description: str
    content: str
    published_at: datetime.datetime
    slug: str
    author: str
    tags: List[str]
    cover_image_url: str
    category_name: str
    related_categories_ids: List[int]
    category: Category
    categories: QuerySet[CategoryModel]

    @classmethod
    def from_article_model(cls, *, article: ArticleModel, lang: typing.Optional[str] = None) -> 'Article':
        lang = lang or get_language()
        content = list(content for content in article.content.all() if content.language == lang)[0]
        category_name = list(
            category.title for category in article.category.content.all() if category.language == lang)[0]
        return Article(
            id=article.id,
            title=content.title,
            description=content.description,
            content=content.content,
            published_at=article.published_at,
            slug=article.slug,
            author=article.author.username,
            tags=content.tags.all().values_list('name', flat=True),
            cover_image_url=content.image and content.image.url or article.image.url,
            category_name=category_name,
            related_categories_ids=article.categories.all().values_list('id', flat=True),
            category=Category.from_category_model(category=article.category, lang=lang),
            categories=article.categories
        )
