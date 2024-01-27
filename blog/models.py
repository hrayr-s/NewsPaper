from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Article(models.Model):
    title = models.CharField(max_length=256)
    slug = models.SlugField()
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

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    published = models.BooleanField(default=False)
    published_at = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to='articles')

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['slug', ], name='article_slug_unique')
        ]

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.published and self.published_at is not None:
            raise ValueError('Cannot unpublish article after published!')
        if self.published and self.published_at is None:
            self.published_at = timezone.now()
        super().save(force_insert, force_update, using, update_fields)
