from pathlib import Path
from quickmedia.utils.constants import (
    AUTH_USER_MODEL,
    POSTGRES_URL,
    ROOT_URLS_CONFIG,
    WSGI_APPLICATION,
    TEMPLATES_DIR,
    LANAGUAGE_CODE_EN,
    LANAGUAGE_CODE_FRENCH,
    LANAGUAGE_ARABIC,
    LANAGUAGE_CODE_ARABIC,
    LANAGUAGE_CODE_HINDI,
    LANAGUAGE_CODE_SPANISH,
    LANAGUAGE_EN,
    LANAGUAGE_FRENCH,
    LANAGUAGE_HINDI,
    LANAGUAGE_SPANISH,
    TIMEZONE_INDIA,
    STATIC_DIRS,
    STATIC_ROOT,
    MEDIA_ROOT,
    MEDIA_URL,
    CACHE_TABLE,
    STATIC_URL,
    INTERNAL_IPS,
)
import os
from dotenv import dotenv_values
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent
config = dotenv_values(".env")

# Quick-start development settings - unsuitable for production

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = True

ALLOWED_HOSTS = ["*"]

AUTH_USER_MODEL = AUTH_USER_MODEL

# Application definition

INSTALLED_APPS = [
    "accounts.apps.AccountsConfig",
    "youtube.apps.YoutubeConfig",
    "facebook.apps.FacebookConfig",
    "instagram.apps.InstagramConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django_extensions",
    "phonenumber_field",
    "schema_graph",
    "debug_toolbar",
]


# Debug Toolbar Configurations
INTERNAL_IPS = INTERNAL_IPS

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = ROOT_URLS_CONFIG

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, TEMPLATES_DIR)],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = WSGI_APPLICATION


# Database

DATABASES = {}
DATABASES["default"] = dj_database_url.parse(POSTGRES_URL)

# Password validation

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization

LANGUAGE_CODE = LANAGUAGE_CODE_EN
LANGUAGES = {
    (LANAGUAGE_CODE_EN, LANAGUAGE_EN),
    (LANAGUAGE_CODE_FRENCH, LANAGUAGE_FRENCH),
    (LANAGUAGE_CODE_HINDI, LANAGUAGE_HINDI),
    (LANAGUAGE_CODE_SPANISH, LANAGUAGE_SPANISH),
    (LANAGUAGE_CODE_ARABIC, LANAGUAGE_ARABIC),
}

TIME_ZONE = TIMEZONE_INDIA

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = STATIC_URL
STATICFILES_DIRS = [os.path.join(BASE_DIR, STATIC_DIRS)]
STATIC_ROOT = STATIC_ROOT

MEDIA_URL = MEDIA_URL
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_ROOT)

# Default primary key field type

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# Cache Configurations
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": CACHE_TABLE,
    }
}
