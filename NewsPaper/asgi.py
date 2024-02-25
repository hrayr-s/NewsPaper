"""
ASGI config for NewsPaper project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'Dev')

from configurations.asgi import get_asgi_application  # noqa

application = get_asgi_application()
