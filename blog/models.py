from django.conf import settings
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy, gettext as _
from mptt.models import MPTTModel, TreeForeignKey
from tinymce.models import HTMLField

from accounts.models import Publisher


class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True, db_index=True, verbose_name=gettext_lazy("Tag"))
    language = models.CharField(max_length=4, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)

    def __str__(self):
        return f'{self.name} ({self.language})'


class Category(MPTTModel):
    slug = models.SlugField()
    image = models.ImageField(upload_to='categories')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.slug

    class Meta:
        verbose_name_plural = gettext_lazy('Categories')


class CategoryContent(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='content')
    language = models.CharField(max_length=4, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)

    title = models.CharField(max_length=128)
    image = models.ImageField(
        upload_to='categories',
        null=True,
        blank=True,
        help_text=gettext_lazy("Language specific image. If not set category default image will be taken.")
    )

    class Meta:
        verbose_name_plural = gettext_lazy('Categories Contents')
        verbose_name = gettext_lazy('Category Content')
        unique_together = ('category', 'language')


class Article(models.Model):
    slug = models.SlugField()
    category = models.ForeignKey(
        Category,
        related_name='main_articles',
        on_delete=models.CASCADE,
        verbose_name=gettext_lazy('Main Category'),
        null=False,
        blank=False
    )
    categories = models.ManyToManyField(
        Category, related_name='articles', verbose_name=gettext_lazy('Related Categories'), blank=True)

    author = models.ForeignKey(Publisher, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)

    featured = models.BooleanField(default=False)
    featured_at = models.DateTimeField(blank=True, null=True)

    image = models.ImageField(upload_to='articles')

    def __str__(self):
        return self.slug

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['slug', ], name='article_slug_unique')
        ]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.published and self.published_at is not None:
            raise ValueError(_('Cannot un-publish article after published!'))
        if self.published and self.published_at is None:
            self.published_at = timezone.now()
        if self.featured and self.featured_at is None:
            self.featured_at = timezone.now()
        super().save(force_insert, force_update, using, update_fields)


class ArticleContent(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='content')
    language = models.CharField(max_length=4, choices=settings.LANGUAGES, default=settings.LANGUAGE_CODE)

    title = models.CharField(max_length=256)
    description = models.TextField()

    tags = models.ManyToManyField(Tag, related_name='articles_contents', blank=True)
    image = models.ImageField(upload_to='articles_contents', blank=True, null=True)

    content = HTMLField()

    class Meta:
        verbose_name = gettext_lazy('Articles Contents')
        unique_together = ('article', 'language')
