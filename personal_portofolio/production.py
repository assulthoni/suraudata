# Production settings
from settings.base import *
DEBUG = False
DATABASES = {
      'default': {
    		'ENGINE': 'django.db.backends.postgresql_psycopg2',
    		'NAME': 'suraudat_db_websuraudata',
    		'USER': 'suraudat_jagoandata',
    		'PASSWORD': 'qaua8XD3cR35pXJ' ,
    		'HOST': 'localhost',
    		'PORT': '5432',
      }
}
