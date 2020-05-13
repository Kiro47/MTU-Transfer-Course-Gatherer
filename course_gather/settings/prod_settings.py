from course_gather.settings.base import *  # noqa: F401, F403

SECRET_KEY = os.getenv('SECRET_KEY', '')  # noqa: F405
DEBUG = False
ALLOWED_HOSTS = ['*']

INSTALLED_APPS.insert(0, 'whitenoise.runserver_nostatic')  # noqa: 405
MIDDLEWARE.insert(0, 'whitenoise.middleware.WhiteNoiseMiddleware')  # noqa: 405
