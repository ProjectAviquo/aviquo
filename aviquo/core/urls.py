"""
URL configuration for aviquo project.
"""

from typing import Any, List

from django.contrib import admin
from django.urls import include, path

urlpatterns: List[Any] = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
]
