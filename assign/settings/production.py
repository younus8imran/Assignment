import os 
from . import BASE_DIR 


##  SECRET KEY settings
SECRET_KEY = os.environ.get('SECRET_KEY')

ALLOWED_HOSTS = ['.herokuapp.com']

DEBUG = (os.environ.get('DEBUG_VALUE') == 'True')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.psycopg2',
        'NAME': os.environ.get('NAME'),
        'USER': os.environ.get('USER'),
        'PASSWORD': os.environ.get('PASSWORD'),
        'HOST': os.environ.get('HOST'),
        'PORT': os.environ.get('PORT'),
    }
}