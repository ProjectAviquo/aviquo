"""Chat app config"""
from django.apps import AppConfig


class ChatConfig(AppConfig):
    """Chat configuration"""
    default_auto_field = "django.db.models.BigAutoField"
    name = "chat"
