from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField


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
    category = models.ForeignKey(Category, related_name='main_articles', on_delete=models.CASCADE,
                                 verbose_name='Main Category', null=False, blank=False)
    categories = models.ManyToManyField(Category, related_name='articles', verbose_name='Other Categories', blank=True)
    content = HTMLField()
    description = models.TextField()

    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='articles')

    def __str__(self):
        return self.title

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['slug', ], name='article_slug_unique')
        ]
