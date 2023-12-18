"""
URL configuration for aviquo project.
"""

from typing import Any, List

from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, path

from .settings import DEBUG

urlpatterns: List[Any] = [
    path("admin/", admin.site.urls),
    path("", include("base.urls")),
]

if DEBUG:
    urlpatterns.extend(staticfiles_urlpatterns())
