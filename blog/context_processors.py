from blog.models import Category


def categories(request):
    """
    Adds categories to the template renderer context.
    Return a list of 'Category' model objects
    """
    category_list = Category.objects.filter(level=1).annotate().prefetch_related('content').order_by('content__title')
    return {
        'categories': category_list,
    }
