from blog.models import CategoryContent


def categories(request):
    """
    Adds categories to the template renderer context.
    Return a list of 'Category' model objects
    """
    category_list = CategoryContent.objects.filter(
        category__parent__isnull=True,
        language=request.LANGUAGE_CODE,
    ).annotate().select_related('category').order_by('title')

    return {
        'categories': category_list,
    }
