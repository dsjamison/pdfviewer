import os
from pathlib import Path

from django.contrib.messages import constants as message_constants
from django.core.exceptions import ImproperlyConfigured
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
LOGS_DIR = os.path.join(BASE_DIR, "logs")


def create_logs_directory():
    if not os.path.exists(LOGS_DIR):
        os.makedirs(LOGS_DIR)


create_logs_directory()

MESSAGE_TAGS = {
    message_constants.DEBUG: "secondary",
    message_constants.INFO: "info",
    message_constants.SUCCESS: "success",
    message_constants.WARNING: "warning",
    message_constants.ERROR: "danger",
}


def get_env_variable(var_name):
    try:
        return os.environ[var_name]
    except KeyError as e:
        error_msg = f"Set the environment variable {var_name}"
        raise ImproperlyConfigured(error_msg) from e


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DEBUG")

ALLOWED_HOSTS = ["*"]

CORS_ALLOW_ALL_ORIGINS = True

CSRF_TRUSTED_ORIGINS = [
    "http://localhost:8000",
    "http://127.0.0.1:8000",
]

CSRF_COOKIE_SECURE = True
CSRF_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "pdf_viewer.apps.PdfViewerConfig",
    # "django.contrib.sites",
    # "django.contrib.flatpages",
    # "django.contrib.sitemaps",
    # "django.contrib.humanize",
    # "django.contrib.postgres",
    # "django_extensions",
    # "debug_toolbar",
    # "rest_framework",
    # "corsheaders",
    # Third-party
    # "crispy_forms",
    # "crispy_bootstrap5",
    # "corsheaders",
    # "rest_framework",
    # "rest_framework_api_key",
    # "drf_spectacular",
    # "storages",  # django_storages
    # "widget_tweaks",
    # "django_extensions",
    # "taggit",  # django-taggit
    # 'django_filters',
    # 'waffle',  # django-waffle
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    #  "whitenoise.middleware.WhiteNoiseMiddleware",  # WhiteNoise
    #  "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    # "django.middleware.cache.UpdateCacheMiddleware",
    "django.middleware.common.CommonMiddleware",
    # "django.middleware.cache.FetchFromCacheMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "templates",
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.media",
                "django.template.context_processors.csrf",
                "django.template.context_processors.tz",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
    # "default": {
    #     "ENGINE": "django.db.backends.postgresql",
    #     "NAME": os.getenv("DATABASE_NAME", ""),
    #     "USER": os.getenv("DATABASE_USER", ""),
    #     "PASSWORD": os.getenv("DATABASE_PASSWORD", "None"),
    #     "HOST": os.getenv("DATABASE_HOST", "localhost"),
    #     "PORT": os.getenv("DATABASE_PORT", "5432"),
    # }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    # {
    #     # Checks whether the password contains at least one uppercase letter
    #     'NAME': 'accounts.validators.UppercaseValidator',
    # },
    # {
    #     # Checks whether the password contains at least one lowercase letter
    #     'NAME': 'accounts.validators.LowercaseValidator',
    # },
    # {
    #     # Checks whether the password contains at least one digit
    #     'NAME': 'accounts.validators.DigitValidator',
    # },
    # {
    #     # Checks whether the password contains at least one special character
    #     # (e.g., !@#$%^&*()_+-=[]{}|;:,.<>?)
    #     'NAME': 'accounts.validators.SpecialCharacterValidator',
    # },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
        # "OPTIONS": {
        #     "min_length": 14,  # Minimum length of 14 characters
        # },
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/"

# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

# django-crispy-forms
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# https://django-allauth.readthedocs.io/en/latest/installation.html?highlight=backends
AUTHENTICATION_BACKENDS = [
    "django.contrib.auth.backends.AllowAllUsersModelBackend",
    "django.contrib.auth.backends.ModelBackend",
]

FIXTURE_DIRS = [
    "fixtures",
]

# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#substituting-a-custom-user-model
#AUTH_USER_MODEL = "accounts.User"

# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
#SITE_ID = 1

# django-debug-toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# https://docs.djangoproject.com/en/dev/ref/settings/#internal-ips
INTERNAL_IPS = ["127.0.0.1"]

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_DIR = BASE_DIR / "media"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    "root": {
        "handlers": ["console"],
        "level": "INFO",
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "WARNING"),
            "propagate": True,
        },
    },
}

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": None,
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DATE_FORMAT': '%m/%d/%Y',
    'DATETIME_FORMAT': '%m/%d/%Y %H:%M:%S',
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    'DEFAULT_PERMISSION_CLASSES': (
    ),
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
}

SPECTACULAR_SETTINGS = {
    "TITLE": "PDF Viewer API",
    "DESCRIPTION": "PDF Viewer",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": True,
}

# https://whitenoise.readthedocs.io/en/latest/django.html
# STORAGES = {
#     "default": {
#         "BACKEND": "Z*.storages.TaggedS3Boto3Storage",
#         "OPTIONS": {},
#     },
#     "staticfiles": {
#         "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
#     },
# }

# AWS settings
AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = os.getenv("AWS_STORAGE_BUCKET_NAME")
AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"
AWS_S3_REGION_NAME = os.getenv("AWS_S3_REGION_NAME")
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_LINK_EXPIRATION = 60 * 60 * 12  # Link expires in 12 hours

# taggit options
TAGGIT_CASE_INSENSITIVE = True
KEYWORDS_KEY = 'KeyWords'
ENHANCED_KEYWORDS_KEY = 'EnhancedKeywords'
ACRONYMS_KEY = 'Acronyms'
TAG_DELIMITER = ':'
METADATA_KEYS = ['enhanced_keywords', 'acronyms', 'keywords']

# SQS Queue
SQS_QUEUE_NAME = ""
SQS_QUEUE_URL = ""
SQS_QUEUE_REGION = ""

API_KEY = os.environ.get('API_KEY', 'NONE')

# CACHES = {
#     "default": {
#         "BACKEND": "django_redis.cache.RedisCache",
#         "LOCATION": "redis://localhost:6379/1",  # Database 1
#         "OPTIONS": {
#             "CLIENT_CLASS": "django_redis.client.DefaultClient",
#         }
#     }
# }
#
# CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"
# CELERY_ACCEPT_CONTENT = ["json"]
# CELERY_TASK_SERIALIZER = "json"

