from django.contrib.messages.api import get_messages
from django.contrib.messages.constants import DEFAULT_LEVELS

from blog.models import Category


def categories(request):
    """
    Return a list of 'Category' model objects
    """
    category_list = Category.objects.all().order_by('title')
    return {
        'categories': category_list,
    }
