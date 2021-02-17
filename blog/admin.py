from django.contrib import admin

from blog.forms import ArticleForm
from blog.models import Category, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at', 'updated_at', 'category', 'description')
    search_fields = ('title', 'content')
    list_filter = ('published_at', 'category', 'categories',)
    exclude = ('creator', )
    date_hierarchy = 'published_at'
    form = ArticleForm

    def save_model(self, request, obj, form, change):
        obj.creator = request.user
        return super(ArticleAdmin, self).save_model(request=request, obj=obj, form=form, change=change)


admin.site.register(Category)
admin.site.register(Article, ArticleAdmin)
