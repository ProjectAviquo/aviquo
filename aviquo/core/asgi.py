"""
ASGI Configuration for the entire project
"""

import os

from django.core.asgi import get_asgi_application

from .settings import logging_startup

logging_startup()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

application = get_asgi_application()
