from django.utils.translation import gettext_noop as _

# Settings Constants
POSTGRES_URL = "postgres://mohit-trootech:postgres@localhost:5432/quickmedia"
AUTH_USER_MODEL = "accounts.user"
ROOT_URLS_CONFIG = "quickmedia.urls"
WSGI_APPLICATION = "quickmedia.wsgi.application"
TEMPLATES_DIR = "templates/"
LANAGUAGE_CODE_EN = "en-us"
LANAGUAGE_EN = _("English")
LANAGUAGE_CODE_FRENCH = "fr"
LANAGUAGE_FRENCH = _("French")
LANAGUAGE_CODE_HINDI = "hi"
LANAGUAGE_HINDI = _("Hindi")
LANAGUAGE_CODE_SPANISH = "es"
LANAGUAGE_SPANISH = _("Spanish")
LANAGUAGE_CODE_ARABIC = "ar"
LANAGUAGE_ARABIC = _("Arabic")

TIMEZONE_INDIA = "Asia/Kolkata"
STATIC_DIRS = "templates/static"
STATIC_ROOT = "assets"
STATIC_URL = "static/"
MEDIA_URL = "media/"
MEDIA_ROOT = "media/"
CACHE_TABLE = "quickmedia_cache"

INTERNAL_IPS = ["127.0.0.1"]

# Template Names
INDEX_TEMPLATE = "quickmedia/index.html"

# Url Reverse Names
INDEX_REVERSE = "index"
SCHEMA_REVERSE = "schema"
