"""
Django settings for booctop project.

Generated by 'django-admin startproject' using Django 3.0.6.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

from django.utils.translation import ugettext_lazy as _
from django.core.paginator import Paginator
import environ


# Set the project base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Take environment variables from .env file
environ.Env.read_env()

env = environ.Env(
    DEBUG=(bool, False)
)

READ_DOT_ENV_FILE= env.bool('READ_DOT_ENV_FILE', default=False)
if READ_DOT_ENV_FILE:
    environ.Env.read_env()

DEBUG = env('DEBUG')
# DEBUG = False

SECRET_KEY = env('SECRET_KEY')

ALLOWED_HOSTS = ['*']

# This SMTP config is given from the client directly. Never change it.
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtpout.secureserver.net'
EMAIL_HOST_USER = 'support@booctep.com'
EMAIL_HOST_PASSWORD = 'Booctep1011'
EMAIL_USE_TLS = False
EMAIL_PORT = 465
EMAIL_USE_SSL=True


# Application definition

INSTALLED_APPS = [

    'home',
    'django.contrib.admin',
    # 'django.contrib.admin.apps.SimpleAdminConfig',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_crontab',
    'teacher',
    'student',
    'video',
    'social_django',
    'discount',
    'paypal.standard.ipn',
    'payment',
    'django_social_share',

]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'booctop.middleware.ForceDefaultLanguageMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'booctop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'booctop/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends', # social signup
                'social_django.context_processors.login_redirect',  # and this
            ],
        },
    },
]

WSGI_APPLICATION = 'booctop.wsgi.application'
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Never change db config and commit.
# If you want to use local db, change this config and don't commit to repo.
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'booctop',
        'USER': 'root', # 'root',
        'PASSWORD': 'root',
        'HOST': 'localhost', #'localhost',   # Or an IP Address that your DB is hosted on
        'PORT': '3306',

        # 'ENGINE': 'django.db.backends.mysql',
        # 'NAME': 'booctop',
        # 'USER': 'root', # 'root',
        # 'PASSWORD': '',
        # 'HOST': 'localhost', #'localhost',   # Or an IP Address that your DB is hosted on
        # 'PORT': '3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'ar'

# LANGUAGE_COOKIE_NAME = 'django-language'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True
# STATICFILES_DIRS = (
    # os.path.normpath(os.path.join(BASE_DIR, '/booctop/static/')),
# )

LOCALE_PATHS = (
   os.path.join(BASE_DIR, 'locale'),
   os.path.join(BASE_DIR, 'home/locale'),   
   os.path.join(BASE_DIR, 'teacher/locale'),   
)

LANGUAGES = (
    ('en', _('English')),
    ('ar', _('Arabic')),
)

MULTILINGUAL_LANGUAGES = (    
    "en-us",
    "ar",
)

# PREFIX_DEFAULT_LOCALE = 'ar'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

# STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(BASE_DIR, "booctop/statics")
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


STATIC_URL = '/static/'
# BASE_URL = 'http://127.0.0.1:8000'
BASE_URL = 'booctep.com'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "booctop/static"),
)
SESSION_COOKIE_AGE = 60 * 60 * 24 * 365 * 5  # set session expire time as 5 years

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
SESSION_EXPIRE_AT_BROWSER_CLOSE=False
#whether the session cookie should be secure (https:// only)

SESSION_COOKIE_NAME='sessionid'  # use the sessionid in your views code
SECURE_HSTS_SECONDS = 31536000




AUTH_USER_MODEL = 'home.User'
AUTHENTICATION_BACKENDS = [
    'home.backends.EmailAuthBackend',
    # 'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    # 'social_core.backends.linkedin.LinkedinOAuth2',
    'social_core.backends.instagram.InstagramOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'django.contrib.auth.backends.ModelBackend',
]

# django-paypal settings
# PAYPAL_RECEIVER_EMAIL = 'support@booctep.com' #'sjcdas-facilitator@gmail.com' # 'sb-wtj43p8374977@business.example.com'
PAYPAL_RECEIVER_EMAIL = 'booctepdotcom2030@gmail.com'
PAYPAL_TEST = True

LOGIN_URL = 'login'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'logout'

SOCIAL_AUTH_FACEBOOK_KEY = '466816721163746'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = '2cf20f71ac45a3bb45d4b14214874e7e' # App Secret
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link'] # add this
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {       # add this
  'fields': 'id, name, email, picture.type(large)'
}
SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [ 
    ('email', 'email'),
    ('picture', 'image'),
    ('1', 'group_id'),
]
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1033113077182-430h4m94e4go7b2q9of2mb5mfu88rh85.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '695870330478-vsrte5l4rsf4d5amkm7v5vgd15kts8g3.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1041581575562-f5tiq7l6uaf8mk5suo0m2dhq9krd49r6.apps.googleusercontent.com'
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = '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'

SOCIAL_AUTH_INSTAGRAM_KEY = '267910061521683'         #Client ID
SOCIAL_AUTH_INSTAGRAM_SECRET = '95c0b482253e9eb434b35acfcdb106b5'  #Client SECRET
# SOCIAL_AUTH_INSTAGRAM_EXTRA_DATA = [         ('user', 'user'),]

SOCIAL_AUTH_URL_NAMESPACE = 'social'

VIMEO_TOKEN = '219cb1675d7cffd2eca82a6c9ca86dbb'
VIMEO_KEY = '252b44a621d7c1212a01e13f5737bfe9eb912b83'
VIMEO_SECRET = 'jffm+bdiKCgVh1vVcWwOEwQzX7U+J6e/J1ecHdltMtM4Qgg6KAB4hf4W2oA/b5KPC0V0l65sryTYror1ZHDkSRT+Vxw709RJgyAwkCRQWPEd44qp7ymBDbDRVfF6SGLj'

CRONJOBS = [
    ('0 13 * * *', 'teacher.cron.my_jobs')
]

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt' : "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.FileHandler',
#             'filename': 'mysite.log',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers':['file'],
#             'propagate': True,
#             'level':'DEBUG',
#         },
#         'MYAPP': {
#             'handlers': ['file'],
#             'level': 'DEBUG',
#         },
#     }
# }
