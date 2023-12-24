"""
Admin view for API
Unregisters APIKeys from the DB
"""

from django.contrib import admin
from rest_framework_api_key.admin import APIKey

# Hide the "API Key Permissions" group in the admin to reduce clutter.
# Consider: Enable the group in the future based on the admin user role
admin.site.unregister(APIKey)
