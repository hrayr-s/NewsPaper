from NewsPaper.venv import base_dir, env


class StorageConfig:
    DATABASES = {
        # looks for `DATABASE_URL`.
        # ImproperlyConfigured exception if no cache is set in `.env`.
        'default': env.db()
    }
    CACHES = {
        # Read os.environ['CACHE_URL'] and raises
        # ImproperlyConfigured exception if no cache is set in `.env`.
        'default': env.cache(backend='django_redis.cache.RedisCache'),
    }

    STATIC_URL = '/static/'
    # STATIC_ROOT = base_dir() / 'static'
    STATICFILES_DIRS = [
        base_dir() / "static",
    ]

    MEDIA_ROOT = base_dir() / 'uploads'
    MEDIA_URL = '/uploads/'
