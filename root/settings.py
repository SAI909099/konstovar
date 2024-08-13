from os.path import join
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-rg-@di2g=q^da11am%j0o@pl-ho4$_lk-w19qpmmya*tdo#okv'

DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps',
    'teacher',
    'mathfilters',
    'sorl.thumbnail',
    'django.contrib.humanize',
    'ckeditor',
    'mptt',


]
AUTH_USER_MODEL = 'apps.User'
LOGOUT_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'root.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'roots.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


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


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = join(BASE_DIR,'static')

MEDIA_URL = 'media/'
MEDIA_ROOT = join(BASE_DIR,'media')

CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
JAZZMIN_SETTINGS = {
    "site_title": "Library Admin",

    "site_header": "Library",

    "site_brand": "Alijahon",

    "site_logo": "apps/app/logo_site.png",

    "login_logo": None,

    "login_logo_dark": None,

    "site_logo_classes": "img-circle",

    "site_icon": None,

    "welcome_sign": "Welcome to the library",



    "search_model": ["apps.User", "auth.Group"],



}
