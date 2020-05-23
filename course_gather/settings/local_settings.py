from course_gather.settings.base import *  # noqa: F401, F403

SECRET_KEY = os.getenv('SECRET_KEY', '')  # noqa: F405
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS += (  # noqa: F405
    'corsheaders',
    'debug_toolbar',
)

MIDDLEWARE += (  # noqa: F405
    'corsheaders.middleware.CorsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

CORS_ORIGIN_ALLOW_ALL = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}

# Allow all IPs to view debug toolbar
DEBUG_TOOLBAR_CONFIG = {
    "SHOW_TOOLBAR_CALLBACK" : lambda request: True,
}
