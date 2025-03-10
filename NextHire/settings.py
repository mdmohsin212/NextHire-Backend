from pathlib import Path
import environ
import os
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url
from datetime import timedelta
   

env = environ.Env()

BASE_DIR = Path(__file__).resolve().parent.parent

environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = env("SECRET_KEY")

DEBUG = True

ALLOWED_HOSTS = ["*"]


LOGIN = "https://nexthire-frontend.vercel.app/login"

CSRF_TRUSTED_ORIGINS = ['https://*.127.0.0.1', "https://*.vercel.app", 'https://*.supabase.com']

INSTALLED_APPS = [
    'corsheaders',
    'whitenoise.runserver_nostatic',
    'cloudinary',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'account',
    'resume',
    'job',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:5173",
    "https://nexthire-frontend.vercel.app",
    "https://nexthire-backend.vercel.app",
]


REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend']
}

ROOT_URLCONF = 'NextHire.urls'


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=3),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
}


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

WSGI_APPLICATION = 'NextHire.wsgi.app'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env("dbname"),
        'USER': env("user"),
        'PASSWORD': env("password"),
        'HOST': env("host"),
        'PORT': env("port")
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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CLOUDINARY_URL='cloudinary://731965217684527:ydorUKvuQk3LvAaMm35UgZkOvJM@djigbo7zo'

cloudinary.config( 
    cloud_name = "djigbo7zo", 
    api_key = "731965217684527", 
    api_secret = "ydorUKvuQk3LvAaMm35UgZkOvJM",
    secure=True
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
# EMAIL_HOST_USER = env("EMAIL")
# EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")
EMAIL_HOST_USER = "siam.mohsin2005@gmail.com"
EMAIL_HOST_PASSWORD = "eclhmmxgpgykgmts"
