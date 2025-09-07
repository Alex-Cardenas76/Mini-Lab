"""
Configuración de desarrollo usando SQLite
"""

from .settings import *

# Base de datos SQLite para desarrollo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuraciones adicionales para desarrollo
DEBUG = True
ALLOWED_HOSTS = ['*']

# Configuración de archivos estáticos para desarrollo
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]

# Configuración de archivos de medios para desarrollo
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

print("🔧 Usando configuración de desarrollo con SQLite")
