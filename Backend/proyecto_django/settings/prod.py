import os
import dj_database_url
from .base import *
# Configurar base de datos para Render

DEBUG = os.environ.get("DEBUG", "False") == "True"

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

# Permitir Render
ALLOWED_HOSTS = ["*"]


