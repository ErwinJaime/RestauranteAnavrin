from .base import *

DEBUG = True
ALLOWED_HOSTS = []

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'restauranteAnavrin',
        'USER': 'adminRestaurante',
        'PASSWORD': '12345678',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Static files
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static'] if (BASE_DIR / 'static').exists() else []

MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

# ✅ EMAIL - SendGrid (para testing)
import os

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_API_KEY', '')
DEFAULT_FROM_EMAIL = os.environ.get('EMAIL_FROM', 'erwinnosqui@gmail.com')

if DEBUG:
    print("\n📧 Email: SendGrid configurado")
    print(f"   Backend: {EMAIL_BACKEND}")
    print(f"   From: {DEFAULT_FROM_EMAIL}")
    print(f"   API Key configurada: {bool(EMAIL_HOST_PASSWORD)}\n")