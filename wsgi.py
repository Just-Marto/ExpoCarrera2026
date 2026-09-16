"""
Punto de entrada WSGI para PythonAnywhere.

En la pestaña Web de PythonAnywhere, el archivo WSGI solo tiene que importar esto:
    from wsgi import application
"""
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from run import create_app

application = create_app()
