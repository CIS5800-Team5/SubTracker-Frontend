"""
Django settings for subtracker_frontend project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os
import sys
sys.path.append("libs")

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

LOGIN_URL='/login/'

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ztst0^o1z+svq%0cz(_-5q$f=r#b^s3izn)@(!25^@i=xb7ud8'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['subtracker-ui.azurewebsites.net', 'subtracker.ml', 'www.subtracker.ml', 'localhost','127.0.0.1']

#SITE_ID = 1

# Application definition

INSTALLED_APPS = [
    'social_django',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    #'django.contrib.staticfiles',
    'django.contrib.sites',
    'frontend',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'subtracker_frontend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "social_django.context_processors.backends",
                "social_django.context_processors.login_redirect",
            ],
        },
    },
]

WSGI_APPLICATION = 'subtracker_frontend.wsgi.application'


#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': BASE_DIR / 'db.sqlite3',
#    }
#}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'django_db',
        'USER': 'django_rwx@subtrackerdb',
        'PASSWORD': os.environ['django_rwx_secret'],
        'HOST': 'subtrackerdb.mysql.database.azure.com',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',
    }
}


AUTHENTICATION_BACKENDS = [
    "social_core.backends.azuread_b2c.AzureADB2COAuth2",
    'django.contrib.auth.backends.ModelBackend',
]

SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_ID_KEY = 'userId'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/subscriptions'
SOCIAL_AUTH_LOGIN_ERROR_URL = '/loginerror/'
SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_STRATEGY = 'social_django.strategy.DjangoStrategy'
SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_TENANT_ID = 'ca0de36f-3f37-4d1f-aca1-f7b34698de63'
SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_POLICY = 'B2C_1_cis5800Team5UserFlow'
SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_KEY = '82b69818-6892-43bc-b9ca-8e5589b3cbec'
SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_SECRET = os.environ['azure_auth_secret']
SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_SCOPE = [
    'openid', 'email', 'profile',
        ]
SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_SCHEMA = 'azuread-b2c-oauth2'

SOCIAL_AUTH_PIPELINE = (
    'subtracker_frontend.pipeline.utils.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'subtracker_frontend.pipeline.utils.load_user',
    'social_core.pipeline.social_auth.social_user',
    'subtracker_frontend.pipeline.utils.load_username',
    'subtracker_frontend.pipeline.utils.create_subtracker_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
if 'SOCIAL_AUTH_REDIRECT_IS_HTTPS' in os.environ:
    SOCIAL_AUTH_REDIRECT_IS_HTTPS = os.environ['SOCIAL_AUTH_REDIRECT_IS_HTTPS']
else:
    SOCIAL_AUTH_REDIRECT_IS_HTTPS = False

#SOCIAL_AUTH_AZUREAD_B2C_OAUTH2_USER_FIELDS = [
#    'email', 'fullname'
#    ]


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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

#STATICFILES_LOCATION = "static"
#STATIC_URL = "/static/"

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static")
#]
#STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
#STATIC_ROOT = '/'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

#Email settings
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'subtrackertest@gmail.com'
EMAIL_HOST_PASSWORD ='cis5800subtracker'
EMAIL_USE_TLS = True