'''
Created on Jun 3, 2011

@author: scheper
'''
from django.conf.global_settings import FIXTURE_DIRS


DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'ordering', # Or path to database file if using sqlite3.
        'USER': 'ordering', # Not used with sqlite3.
        'PASSWORD': 'QeFaw7eRus', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

ROOT_URLCONF = 'ordering.urls'

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django_extensions',
    'debug_toolbar',
    'south',
    'ordering',
    'ordering.tests',
)
