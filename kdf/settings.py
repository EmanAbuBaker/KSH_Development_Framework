"""
Django settings for kdf project.

Generated by 'django-admin startproject' using Django 3.2.9.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""


from pathlib import Path


#import library to logging configuration : 
import os
import logging.config
import logging # must be imported in view.py also.
from django.utils.log import DEFAULT_LOGGING

# Internationalization

from django.utils.translation import gettext, ngettext
from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8g-804gv!!s53=a7ahuz#u7pef3#jx@7(r!h1&av=*8f%)a91#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.21.133','localhost', '127.0.0.1', '0.0.0.0']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     # Add our new application framework 
    'framework.apps.FrameworkConfig',#This object was created for us in /framework/apps.py added by eman 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # For localization and translation settings
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kdf.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'kdf.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

#LANGUAGE_CODE = 'en-us'

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Here specified the languages we want our project to be available in
LANGUAGES = (
    ('en', _('English')),
    ('fr', _('French')),
    ('ar', _('Arabic')),
)

# locale path directory for your application where message files will reside

LOCALE_PATHS = [
    BASE_DIR / 'locale/',
]


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

'''
# Configuring logging settings:
# Disabling logging configuration below settings only when need to disable default django logging :
# LOGGING_CONFIG = None
# logging.config.dictConfig(...)
# below are configuration logging settings:
LOGGING = {
    'version': 1, # version of logging
    'disable_existing_loggers': False, 
    # If the disable_existing_loggers key in the LOGGING dictConfig is set to True 
    # (which is the dictConfig default if the key is missing) then all loggers from the default 
    # configuration will be disabled. Disabled loggers are not the same as removed;
    # the logger will still exist, but will silently discard anything logged to it,
    # not even propagating entries to a parent logger.
    "handlers" : { 
        "file": {
            "level": "DEBUG", #This log level describes the severity of the messages that the logger will handle
            "class": "logging.FileHandler",#writes all logging from the django named logger to a local file.
            #"class":"logging.handlers.TimedRotatingFileHandler",# when need to create file every specific period
            #"when": "m", # this specifies the interval hour "h" day "d" , minuites "m" ,seconds "s".
            #'interval': 1, # defaults to 1, only necessary for other values 
            #'backupCount': 1, # how many backup file to keep, 1 per day
            "filename": BASE_DIR / 'django.log', #local logging file name. and path.
            "formatter": "test_format", 
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True
        },
    },
    "formatters": {
        # log record needs to be rendered as text. Formatters describe the exact format of that text
        "test_format": {
            "format": (
                u"[%(asctime)s] [%(levelname)-4s] "
                "(%(module)s.%(funcName)s) %(message)s"
            ),
            "datefmt": "%Y-%m-%d %H:%M:%S %p %Z %z",
        },
    },  
}
'''