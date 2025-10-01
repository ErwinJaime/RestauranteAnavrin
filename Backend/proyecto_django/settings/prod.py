from base import *  # noqa
import os
import dj_database_url


DEBUG = False

ALLOWED_HOSTS = ('*')


DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True
    )
}

# Archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Seguridad
ALLOWED_HOSTS = ["*"]  # O mejor el dominio/subdominio que Render te dé