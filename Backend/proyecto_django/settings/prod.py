import os
import dj_database_url
from .base import *  # Importa la configuración base

DEBUG = False

# Hosts permitidos (Render te da un dominio, pero "*" funciona mientras pruebas)
ALLOWED_HOSTS = ["*"]

# Base de datos - Render provee DATABASE_URL automáticamente
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv("DATABASE_URL"),
        conn_max_age=600,
        ssl_require=True
    )
}

# Archivos estáticos
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Archivos multimedia (opcional, si los usas)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
