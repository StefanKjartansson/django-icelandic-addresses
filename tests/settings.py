import warnings
warnings.filterwarnings(
        'error', r"DateTimeField received a naive datetime",
        RuntimeWarning, r'django\.db\.models\.fields')

import os
import sys

# import source code dir
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), os.pardir))

from django.utils.crypto import get_random_string

chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'

SECRET_KEY = get_random_string(50, chars)

SITE_ID = 300

DEBUG = True
TEMPLATE_DEBUG = DEBUG

BACKENDS = {
    'mysql': 'mysql',
    'postgres': 'postgresql_psycopg2',
    'sqlite': 'sqlite3',
}

MIDDLEWARE_CLASSES = []

DB_TYPE = BACKENDS.get(os.environ.get("DB", 'postgres'))


DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.%s' % DB_TYPE,
            'NAME': 'ice_address',
            }
        }


if DB_TYPE == 'sqlite3':
    DATABASES['default']['NAME'] = ':memory:'


INSTALLED_APPS = (
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
)

import django
version_info = list(map(int, django.get_version().split('.')))
if version_info[0] == 1 and version_info[1] < 7:
    INSTALLED_APPS += ('south',)

INSTALLED_APPS += ('ice_addresses',)

USE_TZ = True
TIME_ZONE = 'UTC'

try:
    from psycopg2cffi import compat
    compat.register()
except ImportError:
    pass
