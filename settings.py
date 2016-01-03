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

import os
BASE_DIR = os.path.dirname(__file__)


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-b+&3%*nxun2l+id*85aou#vpkw%uhd3ko&b06jmkr#ke)6k3k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'timezone_field',
    'users',
    'utils',
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

WSGI_APPLICATION = 'wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

WEBSITE_URL = 'http://127.0.0.1:8000/'
LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Brussels'
USE_I18N = True
USE_L10N = True
USE_TZ = True
AUTH_PROFILE_MODULE = 'users.UserProfile'

EMAIL_USE_TLS = False
EMAIL_HOST = 'localhost'
EMAIL_PORT = 25
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
DEFAULT_FROM_EMAIL = 'foxugly@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

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
    (1, _(u'Médecine Générale')),
    (2, _(u'Pédiatrie')),
    (3, _(u'ORL')),
    (4, _(u'Cardiologue')),
    (5, _(u'Dentiste')),
    (13, _(u'Infirmier(ère) indépendant(e)')),
    (14, _(u'Kinésithérapeute')),
    (15, _(u'Ostéopathe')),
)
TITLE_CHOICES = (
    (1, _(u'Professeur')),
    (2, _(u'Docteur')),
    (3, _(u'Madame')),
    (4, _(u'Monsieur')),
)

SLOT_TYPE = (
    (1, _(u'National Health Pricing Slot')),
    (2, _(u'Free Pricing Slot')),
    (3, _(u'Home visit Slot')),
    (4, _(u'Nursing home Slot')),
)

TYPE_OFFER = (
    (1, _(u'Free')),
    (2, _(u'Standard')),
    (3, _(u'Premium')),
)

SLOT_COLOR = ['#73B5EB', '#94F7CE', '#D798E2', '#FFE68F', ]

DEFAULT_LANGUAGE = 1

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

IMAGE_UPLOAD_PATH = 'pic/'
STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]
ADMIN_MEDIA_PREFIX = '/static/admin/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
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
