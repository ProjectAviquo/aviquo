"""Main app config"""
from django.apps import AppConfig


class MainConfig(AppConfig):
    """Main DB for app"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "main"
