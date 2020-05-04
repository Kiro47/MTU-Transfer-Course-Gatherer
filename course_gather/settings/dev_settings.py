from course_gather.settings.base import *  # noqa: F401, F403
SECRET_KEY = os.getenv('SECRET_KEY', '')
DEBUG = True
