# urls.py

## Overview

Urls of the server, mostly imports urls from other apps

## Module objects

### Variables

#### urlpatterns

:   URLs used/imported:

    * `admin/` - Django admin pages
    * [main.urls](../main/urls.md)
    * `api/` - [api.urls](../api/urls.md)
    * Media files at [core.settings.MEDIA_URL](./settings.md#media_url) served from [core.settings.MEDIA_ROOT](./settings.md#media_root)
    * If debug: add dev static files
