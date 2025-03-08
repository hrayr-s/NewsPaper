"""NewsPaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
# from django_otp.admin import OTPAdminSite
from django.urls import path, include, re_path

from NewsPaper.choices import EnvChoices

# admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('', include('blog.urls', namespace='blog')),
]

if settings.ENVIRONMENT == EnvChoices.local:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        urlpatterns += [
            path("__debug__/", include('debug_toolbar.urls')),
        ]
    if 'rosetta' in settings.INSTALLED_APPS:
        urlpatterns += [
            re_path(r'^rosetta/', include('rosetta.urls'))
        ]
