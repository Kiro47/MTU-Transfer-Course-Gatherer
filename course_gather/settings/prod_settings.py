import os
from course_gather.settings.base import *  # noqa: F401, F403

SECRET_KEY = os.getenv('SECRET_KEY', '')
DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS.insert(0, 'whitenoise.runserver_nostatic')  # noqa: 405

# Insert after django.middleware.gzip.GZipMiddleware
MIDDLEWARE.insert(2, 'django.middleware.cache.UpdateCacheMiddleware')  # noqa: 405
MIDDLEWARE.insert(2, 'whitenoise.middleware.WhiteNoiseMiddleware')  # noqa: 405

MIDDLEWARE.append('django.middleware.cache.FetchFromCacheMiddleware')  # noqa: 405

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': int(os.getenv('DB_PORT', '5432'))
    }
}

# Tell browser to cache static files forever.
# (Static files have hashes appended to them during the build process.)
WHITENOISE_MAX_AGE = 60 * 10000000

# Cache database table
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'cache',
    }
}

# Cache Django responses for 15 minutes
CACHE_MIDDLEWARE_SECONDS = 60 * 15
