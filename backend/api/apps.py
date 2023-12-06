"""API Apps"""
from django.apps import AppConfig


class ApiConfig(AppConfig):
    """Configure the API to the DB"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api'
