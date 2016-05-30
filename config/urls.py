"""soul_sign URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from sign.urls import urlpatterns as sign_urls
from sign.views import hello_world
from account.urls import patterns as account_urls
from .routers import router

ADMIN_ENDPOINT = 'ultrasecretadmin'

urlpatterns = [
    url(r'^account/', include(account_urls, namespace='account')),
    url(r'^sign/', include(sign_urls)),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', include('rest_framework_social_oauth2.urls')),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^$', hello_world),
    url(r'^' + ADMIN_ENDPOINT + '/', admin.site.urls),
    url(r'^' + ADMIN_ENDPOINT + '/rq/', include('django_rq_dashboard.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = _('Soul Sign Admin Site')