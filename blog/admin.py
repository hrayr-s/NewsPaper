from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from blog.forms import ArticleForm
from blog.models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('slug', 'published_at', 'updated_at', 'category')
    search_fields = ('content__title', 'content__description', 'content__content')
    list_filter = ('published_at', 'category', 'categories',)
    exclude = ('creator', )
    date_hierarchy = 'published_at'
    form = ArticleForm

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super(ArticleAdmin, self).save_model(request=request, obj=obj, form=form, change=change)


admin.site.register(Category, MPTTModelAdmin)
admin.site.register(Article, ArticleAdmin)
