import os


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

SECRET_KEY = 'qkgmy=7$3m%nf=x^fnou4kw2ugmpa3_+b3i&fuk#fk2$by!@nq'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Kiev'
