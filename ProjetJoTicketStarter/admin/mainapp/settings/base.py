"""
https://docs.djangoproject.com/fr/3.2/topics/settings/
"""

from pathlib import Path
from dotenv import load_dotenv
import os
# from  django.contrib.auth.models import User 

# AUTH_USER_MODEL=User
# Récupération du .env
load_dotenv()

DATABASE_HOST = os.getenv('DATABASE_HOST') or '127.0.0.1'
DATABASE_PORT = os.getenv('DATABASE_PORT') or 3307
DATABASE_NAME = os.getenv('DATABASE_NAME') or 'jo_project'
DATABASE_USER = os.getenv('DATABASE_USER') or 'root'
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD') or 'your_password'


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Pensez à générer une nouvelle clé à l'aide de https://djecrety.ir/
SECRET_KEY = "velicyjh0)jmde&@qj=_)hzik!&sw4ml8b92ni&!y@=cu(-hj8"


INSTALLED_APPS = [
    # On explicite l"usage de notre application pour que les templates
    # soient détectés automatiquement par Django
    "corsheaders",
    "mainapp.apps.MainappConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

# Les URLs sont désormais déclarées dans leur propre module
ROOT_URLCONF = "mainapp.urls"

WSGI_APPLICATION = "mainapp.wsgi.application"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
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

# Database
# https://docs.djangoproject.com/fr/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        # !!! A remplacer avec vos informations de connexion !!!
        'NAME': DATABASE_NAME,
        'HOST': DATABASE_HOST,
        'USER' : DATABASE_USER,
        'PASSWORD': DATABASE_PASSWORD,
        'PORT': DATABASE_PORT,
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            # Force use of TCP connection instead of socket
            'unix_socket': '',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/fr/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/fr/3.2/topics/i18n/

LANGUAGE_CODE = "fr-fr"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/fr/3.2/howto/static-files/

STATIC_URL = "/static/"

# Default primary key field type
# https://docs.djangoproject.com/fr/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# GESTION DES AUTORISATIONS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    "http://127.0.0.1:3000",  # Adresse URL local sur le port liveserver
    "http://localhost:3000",  # Adresse URL local sur le port liveserver
]
ALLOWED_HOSTS = [
    '127.0.0.1',  # Pour les tests en local
    'localhost',  # Pour les tests en local
]
