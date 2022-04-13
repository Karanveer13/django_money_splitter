"""
Django settings for money_splitter project.

Generated by 'django-admin startproject' using Django 4.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""
import os
from pathlib import Path
from . info import *

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

EMAIL_USE_TLC = EMAIL_USE_TLC
EMAIL_HOST = EMAIL_HOST
EMAIL_HOST_USER = EMAIL_HOST_USER
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD
EMAIL_PORT = EMAIL_PORT


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8livpb-366)0k*6zl)z6sr#49q1k!h%4%j)6)m=cu#5%d2_pnj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TASTYPIE_FULL_DEBUG = False

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'expenser-app-django-heroku.herokuapp.com']
#ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "127.0.0.1,localhost").split(",")

# From Google https://expenser-app-django-heroku.herokuapp.com/
# From Terminal/Firefox
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'splitter',
    'tastypie',
    'tastypie_swagger',
    #'allauth',
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

# CORS_ORIGIN_WHITELIST = [
#     'http://localhost:5500',
#     'http://127.0.0.1:5500'
# ]

ROOT_URLCONF = 'money_splitter.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'money_splitter.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
# }

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'splitter',
#         'USER': 'Karanveer',
#         'PASSWORD': '123456',
#         'HOST': 'localhost',
#         'PORT': '',
#     }
# }

#postgres://ucinxdojytcwgj:c927b1a5132524831ace13f01f38f2c02142ca479d79cb0aeafb9ddf97fa6d5c@ec2-54-173-77-184.compute-1.amazonaws.com:5432/d6t8v3jin1pml
#postgres://yihsatrfvblsab:bc6d6e22baf9e9ca7c67e95fc674e8b6f15e9cae2941fe834fc6d7bd4cef5870@ec2-54-158-247-210.compute-1.amazonaws.com:5432/d2ep16s0ic9h4d

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'd2ep16s0ic9h4d',
        'USER': 'yihsatrfvblsab',
        'PASSWORD': 'bc6d6e22baf9e9ca7c67e95fc674e8b6f15e9cae2941fe834fc6d7bd4cef5870',
        'HOST': 'ec2-54-158-247-210.compute-1.amazonaws.com',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]


#AUTH_USER_MODEL = 'splitter.User'


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'django.contrib.staticfiles.finders.DefaultStorageFinder',
)




import django_heroku
django_heroku.settings(locals())

API_LIMIT_PER_PAGE = 0