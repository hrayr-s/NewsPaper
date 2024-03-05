from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from blog.forms import ArticleForm
from blog.models import Category, Article, ArticleContent, CategoryContent, Tag


class ArticleContentInline(admin.StackedInline):
    model = ArticleContent
    extra = 0
    min_num = 3
    max_num = 3


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

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super(ArticleAdmin, self).save_model(request=request, obj=obj, form=form, change=change)


class CategoryContentInline(admin.StackedInline):
    model = CategoryContent
    extra = 0
    min_num = 3
    max_num = 3


class CategoryAdmin(MPTTModelAdmin):
    list_display = ('slug', 'parent')
    list_filter = ('parent',)
    inlines = [CategoryContentInline]


admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
