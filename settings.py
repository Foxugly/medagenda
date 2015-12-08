# -*- coding: utf-8 -*-
#
# Copyright 2015, Foxugly. All rights reserved.
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.

from django.utils.translation import ugettext_lazy as _

"""
Django settings for medagenda project.
For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/
For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(__file__)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-b+&3%*nxun2l+id*85aou#vpkw%uhd3ko&b06jmkr#ke)6k3k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'users',
    'utils',
    'colorfield',
    'address',
    'agenda',
    'patient',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

ROOT_URLCONF = 'urls'

WSGI_APPLICATION = 'wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

WEBSITE_URL = 'http://127.0.0.1:8000/'
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Paris'
USE_I18N = True
USE_L10N = True
USE_TZ = True
AUTH_PROFILE_MODULE = 'users.UserProfile'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/user/login/'

FULLCALENDAR_REF_DATE = '2016-02-01'
FULLCALENDAR_REF_DATEFORMAT = '%Y-%m-%d'

LANGUAGES = (
    ('fr', _('Francais')),
    ('nl', _('Nederlands')),
    ('en', _('English')),
)

DAY_CHOICES = (
    (1, _(u'Lundi')),
    (2, _(u'Mardi')),
    (3, _(u'Mercredi')),
    (4, _(u'Jeudi')),
    (5, _(u'Vendredi')),
    (6, _(u'Samedi')),
    (7, _(u'Dimanche')),
)

MEDECINE_CHOICES = (
    (1, _(u'Aucune')),
    (2, _(u'Médecine Générale')),
    (3, _(u'Médecine Interne')),
)
TITLE_CHOICES = (
    (1, _(u'Professeur')),
    (2, _(u'Docteur')),
    (3, _(u'Madame')),
    (4, _(u'Monsieur')),
)

DEFAULT_LANGUAGE = 1

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
#UPLOAD_DIR = 'upload'
#STOCK_DIR = 'folders'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

ADMIN_MEDIA_PREFIX = '/static/admin/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

#TEMPLATE_LOADERS = (
#    'django.template.loaders.filesystem.Loader',
#    'django.template.loaders.app_directories.Loader',
#    # 'django.template.loaders.eggs.Loader',
#)


ROOT_URLCONF = 'urls'

#TEMPLATE_DIRS = (
#    os.path.join(BASE_DIR, 'templates'),
    # '%s/templates/' % BASE_DIR,
#)

#TEMPLATE_CONTEXT_PROCESSORS = (
#    'django.core.context_processors.request',
#    'django.contrib.auth.context_processors.auth',
#    'django.core.context_processors.i18n',
#    'django.core.context_processors.static',
#)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # Insert your TEMPLATE_CONTEXT_PROCESSORS here or use this
                # list if you haven't customized them:
                'django.core.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}