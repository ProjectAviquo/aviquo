"""
App config for the Base app, the basic functions (like auth, profile)
"""
from django.apps import AppConfig


class BaseConfig(AppConfig):
    """Configuration for the Base App

    The app contains basic website stuff, like:
    * Authenitcation
    * Profile management"""

    default_auto_field = "django.db.models.BigAutoField"
    name = "base"
