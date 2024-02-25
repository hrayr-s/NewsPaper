from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone
from mptt.models import MPTTModel, TreeForeignKey
from django.utils.translation import gettext_lazy


class Tag(models.Model):
    name = models.CharField(max_length=25, unique=True, db_index=True, verbose_name=gettext_lazy("Tag"))
    language = models.CharField(max_length=4)


class Category(MPTTModel):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    image = models.ImageField(upload_to='categories')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subcategories')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Article(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    tags = models.ManyToManyField(Tag, related_name='articles', blank=True)
    category = models.ForeignKey(
        Category,
        related_name='main_articles',
        on_delete=models.CASCADE,
        verbose_name='Main Category',
        null=False,
        blank=False
    )
    categories = models.ManyToManyField(
        Category, related_name='articles', verbose_name='Related Categories', blank=True)
    content = HTMLField()
    description = models.TextField()

    author = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)

    featured = models.BooleanField(default=False)
    featured_at = models.DateTimeField(blank=True, null=True)

    image = models.ImageField(upload_to='articles')

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['slug', ], name='article_slug_unique')
        ]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.published and self.published_at is not None:
            raise ValueError('Cannot un-publish article after published!')
        if self.published and self.published_at is None:
            self.published_at = timezone.now()
        if self.featured and self.featured_at is None:
            self.featured_at = timezone.now()
        super().save(force_insert, force_update, using, update_fields)
