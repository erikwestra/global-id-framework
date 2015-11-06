""" gidFramework.settings

    This module contains the Django settings for the GIDFramework project.
"""
import os

import dj_database_url

from gidFramework.shared.lib.settingsImporter import SettingsImporter

#############################################################################

# The base directory for our project:

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#############################################################################

# Load our various custom settings:

import_setting = SettingsImporter(
                    globals(),
                    custom_settings="gidFramework.custom_settings",
                    env_prefix="gid")

import_setting("DEBUG",        True)
import_setting("TIME_ZONE",    "UTC")
import_setting("DATABASE_URL", None)

#############################################################################

# Our various project settings:

SECRET_KEY = 'b150)2elles97mea70p9u5pbffb)qesx1l3=8qp($2xi)=5b50'

ALLOWED_HOSTS = []

INSTALLED_APPS = (
    #'django.contrib.admin',
    #'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    #'django.contrib.auth.middleware.AuthenticationMiddleware',
    #'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'gidFramework.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                #'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'gidFramework.wsgi.application'

DATABASES = {'default': dj_database_url.config(default=DATABASE_URL)}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
