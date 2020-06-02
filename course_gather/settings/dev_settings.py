import os
from course_gather.settings.base import *  # noqa: F401, F403

SECRET_KEY = os.getenv('SECRET_KEY', '')
DEBUG = True

INSTALLED_APPS += (  # noqa: F405
    'corsheaders',
    'debug_toolbar',
)

MIDDLEWARE += (  # noqa: F405
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] += (  # noqa: F405
    'rest_framework.renderers.BrowsableAPIRenderer',
)

CORS_ORIGIN_ALLOW_ALL = True

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

# Allow all IPs to view debug toolbar
DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': lambda request: True,
}
