"""WSGI config for aviquo project.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "aviquo.settings")

application = get_wsgi_application()
