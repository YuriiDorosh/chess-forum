from .base import *

DEBUG = False

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "dbname",
        "USER": "dbuser",
        "PASSWORD": "pass",
        "HOST": "database",
        "PORT": "5432",
    }
}