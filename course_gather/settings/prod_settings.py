import os
from course_gather.settings.base import *  # noqa: F401, F403

SECRET_KEY = os.getenv('SECRET_KEY', '')
DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS.insert(0, 'whitenoise.runserver_nostatic')  # noqa: 405
MIDDLEWARE.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware')  # noqa: 405

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
