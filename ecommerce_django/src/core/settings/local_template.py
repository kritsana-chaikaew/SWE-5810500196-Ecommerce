"""
Django local settings template for core project
"""

DEBUG = True

SECRET_KEY = ":Q'c5Rz`Vz9#sw6W+kW/MTB$0Dzd<6B);[hMjKywU,OoPdOp1C^77r_sjSGz"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'djangoecomm',
        'USER': 'djangoecomm',
        'PASSWORD': 'djangoecomm',
    }
}

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = ''
EMAIL_HOST_PASSWORD = ''
EMAIL_PORT = 587
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True

ALLOWED_HOSTS = ["*"]
