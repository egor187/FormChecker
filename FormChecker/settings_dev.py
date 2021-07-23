from .settings import *


DEBUG = True

ALLOWED_HOSTS = ['*']

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')

INTERNAL_IPS = [
    '127.0.0.1',
]
