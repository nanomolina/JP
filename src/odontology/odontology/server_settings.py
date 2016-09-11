from odontology.settings import *
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'h0_%$7qsz@i-^7_&tcl0_xayt1ce46&20d2#xw=jhvn+gfpm45'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['www.dentalsoft.com.ar']


# Application definition

INSTALLED_APPS = INSTALLED_APPS + []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'odontology',
        'USER': 'nanomolina',
        'PASSWORD': 'nano1234',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = DEFAULT_FROM_EMAIL = 'notifications.dentalsoft@gmail.com'
EMAIL_HOST_PASSWORD = 'dentalsoft1'

ADMINS = (
    ('Nano', 'nanomolinacav@gmail.com'),
)
MANAGERS = ADMINS
SERVER_EMAIL = 'notifications.dentalsoft@gmail.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
SEND_BROKEN_LINK_EMAILS=True
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
