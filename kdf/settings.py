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


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8g-804gv!!s53=a7ahuz#u7pef3#jx@7(r!h1&av=*8f%)a91#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['192.168.21.133','localhost', '127.0.0.1','192.168.41.136']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # configure the accounts app 
    'accounts.apps.AccountsConfig'
     # Add our new application framework 
    #'framework.apps.FrameworkConfig',#This object was created for us in /framework/apps.py added by eman 
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
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
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'KSHdatabase',
        'USER': 'sittana',
        'PASSWORD': 'Sittana@123#',
        'HOST': '127.0.0.1',
        'PORT': '3306',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


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



# LDAP CONFIGRATION START HERE !
# fist import the needed packages
import ldap
from django_auth_ldap.config import LDAPSearch
from django_auth_ldap.config import ActiveDirectoryGroupType


AUTH_LDAP_SERVER_URI = 'ldap://192.168.41.146'

AUTH_LDAP_BIND_DN = "CN=bind,CN=Users,DC=BD,DC=COM"
AUTH_LDAP_BIND_PASSWORD = "Abc123++"
AUTH_LDAP_USER_SEARCH = LDAPSearch(
            "dc=BD,dc=COM", ldap.SCOPE_SUBTREE, "sAMAccountName=%(user)s"
            )

AUTH_LDAP_USER_ATTR_MAP = {
            "username": "sAMAccountName",
                "first_name": "givenName",
                    "last_name": "sn",
                        "email": "mail",
}

AUTH_LDAP_GROUP_SEARCH = LDAPSearch(
            "dc=BD,dc=COM", ldap.SCOPE_SUBTREE, "(objectCategory=Group)"
            )
AUTH_LDAP_GROUP_TYPE = ActiveDirectoryGroupType(name_attr="cn")
AUTH_LDAP_USER_FLAGS_BY_GROUP = {
            "is_superuser": "CN=django-admin,CN=Users,DC=BD,DC=COM",
            "is_staff": "CN=django-admin,CN=Users,DC=BD,DC=COM",
            }
AUTH_LDAP_FIND_GROUP_PERMS = True
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 1  # 1 hour cache

AUTHENTICATION_BACKENDS = [
            'django_auth_ldap.backend.LDAPBackend',
                'django.contrib.auth.backends.ModelBackend',
]



# LDAP CONFIGRATION ENDS HERE !