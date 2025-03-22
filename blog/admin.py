import re
from copy import deepcopy

from django.conf import settings
from django.contrib import admin
from django.contrib import messages
from django.db.transaction import atomic
from django.utils.translation import ngettext
from mptt.admin import MPTTModelAdmin

from blog.forms import ArticleForm
from blog.models import Category, Article, ArticleContent, CategoryContent, Tag


class ArticleContentInline(admin.StackedInline):
    model = ArticleContent
    extra = 0

    @property
    def min_num(self):
        return len(settings.LANGUAGES)

    @property
    def max_num(self):
        return len(settings.LANGUAGES)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'published_at', 'updated_at', 'category')
    search_fields = ('content__title', 'content__description', 'content__content')
    list_filter = ('published_at', 'category', 'categories',)
    exclude = ('author',)
    readonly_fields = ('created_at', 'updated_at', 'published_at')
    date_hierarchy = 'published_at'
    form = ArticleForm
    inlines = [ArticleContentInline]
    prepopulated_fields = {'slug': ('slug',), }
    actions = ['duplicate_records']

    def save_model(self, request, obj, form, change):
        obj.author = request.user.get_or_create_publisher()
        return super(ArticleAdmin, self).save_model(request=request, obj=obj, form=form, change=change)

    @admin.action(description='Duplicate selected records')
    def duplicate_records(self, request, queryset):
        failed_articles = []

        def _count_copy_slug(slug: str):
            if slug.endswith('copy'):
                return f"{slug[:-4]}-1"

            needed_match = None
            for i in re.finditer(r'copy-\d+$', slug):
                needed_match = i

            if needed_match is None or needed_match.end() < len(slug):
                return f"{slug}-copy"

            start, end = needed_match.span()
            num = int(slug[start:end].split('-')[1]) + 1
            return f"{slug[:start]}copy-{num}"

        def _count_copy_title(title: str):
            if title.endswith('(copy)'):
                return f"{title[:-6]}(copy-1)"

            needed_match = None
            for i in re.finditer(r'\(copy-\d+\)$', title):
                needed_match = i

            if needed_match is None or needed_match.end() < len(title):
                return f"{title} (copy)"
            start, end = needed_match.span()
            num = int(title[start:end].split('-')[1][:-1]) + 1
            return f"{title[:start]}(copy-{num})"

        for obj in queryset:
            try:
                with atomic():
                    obj_copy = deepcopy(obj)
                    obj_copy.pk = None
                    obj_copy.slug = _count_copy_slug(obj.slug)
                    obj_copy.save()
                    for content in obj.content.all():
                        content_copy = deepcopy(content)
                        content_copy.pk = None
                        content_copy.title = _count_copy_title(content.title)
                        content_copy.article = obj_copy
                        content_copy.save()
            except Exception:
                failed_articles.append(obj)

        self.message_user(request, ngettext(
            '%d record was successfully duplicated.',
            '%d records were successfully duplicated.',
            queryset.count(),
        ) % queryset.count(), messages.SUCCESS)
        if failed_articles:
            self.message_user(request, ngettext(
                '%d record failed to duplicate.',
                '%d records failed to duplicate.',
                len(failed_articles),
            ) % len(failed_articles), messages.WARNING)


class CategoryContentInline(admin.StackedInline):
    model = CategoryContent
    extra = 0

    @property
    def min_num(self):
        return len(settings.LANGUAGES)

    @property
    def max_num(self):
        return len(settings.LANGUAGES)


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('slug', 'parent')
    list_filter = ('parent',)
    inlines = [CategoryContentInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
