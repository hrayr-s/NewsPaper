from django import forms

from blog.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'

    def clean(self):
        super(ArticleForm, self).clean()
        main_category = self.cleaned_data.get('category')
        categories = self.cleaned_data.get('categories')

        if main_category in categories:
            self.add_error('categories', 'Main category cannot be chosen in related category!')
