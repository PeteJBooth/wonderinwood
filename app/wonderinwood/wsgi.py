"""
WSGI config for wonderinwood project.
"""
import os
from os.path import abspath, dirname
from sys import path

SITE_ROOT = dirname(dirname(abspath(__file__)))
path.append(SITE_ROOT)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wonderinwood.settings')
os.environ.setdefault('DJANGO_CONFIGURATION', 'DevSettings')

from configurations.wsgi import get_wsgi_application

application = get_wsgi_application()
