"""
Here goes all settings for django localization
"""
import os

from NewsPaper.venv import base_dir


class LocaleConfig:
    # Internationalization
    # https://docs.djangoproject.com/en/4.2/topics/i18n/

    LANGUAGE_CODE = os.getenv('DEFAULT_LANGUAGE_CODE', 'en')
    LANGUAGE_COOKIE_NAME = 'language'

    @property
    def LANGUAGES(self):
        try:
            env_languages = os.getenv('LANGUAGES_LIST', None)
            if env_languages:
                language_pairs = env_languages.split(',')
                language_pairs = tuple(map(lambda v: tuple(i.strip() for i in v.split('|')), language_pairs))
                return language_pairs
        except:
            pass
        return (
            ('en', 'English'),
            ('hy', 'Հայերեն'),
            ('ru', 'Русский')
        )

    TIME_ZONE = 'UTC'

    USE_I18N = True

    USE_L10N = True
    LOCALE_PATHS = [
        'locale',
        os.path.join(base_dir(), 'locale')
    ]

    USE_TZ = True
