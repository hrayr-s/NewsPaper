"""
Here goes all settings for django localization
"""
import os

from NewsPaper.venv import base_dir


class LocaleConfig:
    # Internationalization
    # https://docs.djangoproject.com/en/4.2/topics/i18n/

    LANGUAGE_CODE = 'en'
    LANGUAGE_COOKIE_NAME = 'language'
    LANGUAGES = (
        ('en', 'English'),
        ('hy', 'Հայերեն'),
        ('ru', 'Русский')
    )

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True
    LOCALE_PATHS = [
        os.path.join(base_dir(), 'locale')
    ]

    USE_TZ = True
