
'''
Rename this file for settings_env.py
Put here the settings for the proper environment: dev, homolog, prod, etc
'''
import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DEBUG = os.environ.get("ENVIRONMENT", 'development') == 'development'

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': '<DATABASE/>',
#         'USER': '<USER/>',
#         'PASSWORD': '<PASSWORD/>',
#         'HOST': '<HOST/>',
#         'PORT':'5432'
#     }
# }
