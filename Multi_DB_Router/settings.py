"""
Django settings for Multi_DB_Router project.

Generated by 'django-admin startproject' using Django 1.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from six.moves import configparser
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


config = configparser.SafeConfigParser()
config.read(BASE_DIR + '/config.ini')

psqldbpassword = config.get('psql', 'dbpassword')
psqldbuser = config.get('psql', 'dbuser')
mysqldbpassword = config.get('mysql', 'dbpassword')
mysqldbuser = config.get('mysql', 'dbuser')
smtp_host = config.get('smtp', 'host')
smtp_user = config.get('smtp', 'user')
smtp_password = config.get('smtp', 'password')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(lmskztkw-17ftdlg4!_!mpbkej0$h8=n1shufn!rygi%(q4^t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app',
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

ROOT_URLCONF = 'Multi_DB_Router.urls'

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

WSGI_APPLICATION = 'Multi_DB_Router.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {

    'default': {
        'NAME': 'database1',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': psqldbuser,
        'PASSWORD': psqldbpassword
    },
    'database2': {
        'NAME': 'database2',
        'ENGINE': 'django.db.backends.postgresql',
        'USER': psqldbuser,
        'PASSWORD': psqldbpassword
    },
    'database3': {
        'NAME': 'database3',
        'ENGINE': 'django.db.backends.mysql',
        'USER': mysqldbuser,
        'PASSWORD': mysqldbpassword
    },
    'database4': {
        'NAME': 'database4',
        'ENGINE': 'django.db.backends.mysql',
        'USER': mysqldbuser,
        'PASSWORD': mysqldbpassword
    },
    'database5': {
        'NAME': 'database5',
        'ENGINE': 'django.db.backends.mysql',
        'USER': mysqldbuser,
        'PASSWORD': mysqldbpassword
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

LOGIN_URL = '/app/login/'


STATIC_URL = '/static/'
STATIC_ROOT = os.path.join("static",)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = smtp_host
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = smtp_user
EMAIL_HOST_PASSWORD = smtp_password
