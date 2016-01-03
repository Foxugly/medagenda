"""medagenda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from users.views import home, confirm_user
from utils.views import faq, contact, about, lang, offer, conditions
admin.autodiscover()


def custom_404(request):
    return render(request, "404.tpl")


def custom_500(request):
    return render(request, "500.tpl")


urlpatterns = [
    url(r'^confirm/(?P<user_id>[\w-]+)/(?P<text>[\w-]+)/', confirm_user, name='confirm_user'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('users.urls'), name='users'),
    url(r'^doc/', include('users.urls2'), name='users2'),
    url(r'^patient/', include('patient.urls'), name='patient'),
    url(r'^slot/', include('agenda.urls'), name='agenda'),
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^$', home, name='home'),
    url(r'^lang/$', lang, name="lang"),
    url(r'^faq/$', faq, name='faq'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^about/$', about, name='about'),
    url(r'^offer/$', offer, name='offer'),
    url(r'^conditions/$', conditions, name='conditions'),
] \
    + patterns('', (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}), )\
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler404 = 'urls.custom_404'
handler500 = 'urls.custom_500'
