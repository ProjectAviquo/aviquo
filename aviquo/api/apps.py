"""
API App
"""

from django.apps import AppConfig


class ApiConfig(AppConfig):
    """API App Config"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "api"
