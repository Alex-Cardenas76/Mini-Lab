#!/usr/bin/env python
"""
Script para ejecutar el servidor de desarrollo con configuración SQLite
"""

import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fotostudio_system.settings_dev')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "No se pudo importar Django. ¿Está instalado y "
            "disponible en la variable de entorno PYTHONPATH? ¿Olvidaste "
            "activar el entorno virtual?"
        ) from exc
    execute_from_command_line(sys.argv)
