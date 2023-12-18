"""
WSGI config for aviquo project.
"""

import os

from django.core.wsgi import get_wsgi_application

from .settings import logging_startup

logging_startup()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_wsgi_application()
