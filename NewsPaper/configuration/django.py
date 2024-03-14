class DjangoConfig:
    ALLOWED_HOSTS = []
    DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

    @property
    def INSTALLED_APPS(self):
        app_list = [
            'mptt',
            'django.contrib.admin',
            'django.contrib.auth',
            'django.contrib.contenttypes',
            'django.contrib.sessions',
            'django.contrib.messages',
            'django.contrib.staticfiles',

            # 'django_otp',
            # 'django_otp.plugins.otp_totp',
            # 'django_otp.plugins.otp_static',
            'accounts',
            'tinymce',
            'blog',
        ]
        if self.DEBUG:
            app_list.append('debug_toolbar')

        return app_list

    @property
    def MIDDLEWARE(self):
        middleware_list = [
            'django.middleware.security.SecurityMiddleware',
            'django.contrib.sessions.middleware.SessionMiddleware',
            'django.middleware.common.CommonMiddleware',
            'django.middleware.csrf.CsrfViewMiddleware',
            'django.contrib.auth.middleware.AuthenticationMiddleware',
            # 'django_otp.middleware.OTPMiddleware',
            'django.contrib.messages.middleware.MessageMiddleware',
            'django.middleware.clickjacking.XFrameOptionsMiddleware',
        ]

        if self.DEBUG:
            middleware_list.append('debug_toolbar.middleware.DebugToolbarMiddleware')
        return middleware_list

    ROOT_URLCONF = 'NewsPaper.urls'

    WSGI_APPLICATION = 'NewsPaper.wsgi.application'

    AUTH_USER_MODEL = 'accounts.User'
    AUTH_PASSWORD_VALIDATORS = [
        {
            'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
        },
        {
            'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
        },
    ]
