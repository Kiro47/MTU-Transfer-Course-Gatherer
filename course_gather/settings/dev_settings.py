import os
from course_gather.settings.base import *  # noqa: F401, F403

SECRET_KEY = os.getenv('SECRET_KEY', '')
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),  # noqa: F405
    }
}
