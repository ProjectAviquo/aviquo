# settings.py

## Overview

Settings for the entire project

## Module Objects

### Variables

#### BASE_DIR

:   Base source code dir

#### SECRET_KEY

:   Secret key for cryptography and stuff

#### DEBUG

:   Whether server is in debug mode. Django adds more stuff for error messages, etc.

#### INSTALLED_APPS

:   Apps that are installed

    * Django libraries
    * [main.apps.MainConfig](../main/apps.md#mainconfig)
    * [api.apps.ApiConfig](../api/apps.md#apiconfig)
    * [chat.apps.ChatConfig](../chat/apps.md#chatconfig)
    * REST framework
    * REST API key
    * Cors headers

#### LOGIN_REDIRECT_URL

:   Where you are redirected after login, to profile page

#### LOGIN_URL

:   Login url

#### MIDDLEWARE

:   Middleware:

    * Django security
    * Django sessions
    * Django messages
    * Cors headers

#### ROOT_URLCONF

:   Main urls, set to [core.urls](./urls.md)

#### TEMPLATES

:   Template settings

    * Use Django template system
    * Look inside app folders
    * Preprocessors

#### ASGI_APPLICATION

:   The ASGI for the project. Set [core.asgi.application](./asgi.md#application)

#### AUTH_USER_MODEL

:   The user model to use for authentication. Set to [main.User](../main/models.md#user)

#### DATABASES

:   Sqlite3 as database. Database file: backend/db.sqlite3

#### AUTH_PASSWORD_VALIDATORS

:   Password requirements:

    * Minimum length
    * Numeric character

#### REST_FRAMEWORK

:   Settings for the REST API.

:   Permissions:

* Has API Key

#### LANGUAGE_CODE

:   English

#### TIME_ZONE

:   New York (EST)

#### USE_I18N

:   Internationalization - True

#### USE_TZ

:   Use timezone - True

#### STATIC_URL

:   Where the static *url* should start

#### STATIC_ROOT

:   Where the static *files* are located **in production**

!!! warning

    This only affects production. For development (when `DEBUG=True`) each /<appname\>/static folders are used.
    
    Run `python3 manage.py collectstatic` to collect all of the static files into the /backend/static folder.

    Read the the [official documentation](https://docs.djangoproject.com/en/4.2/howto/static-files/) for more info on static files.

#### MEDIA_URL

:   The url for user media (like profile pictures)

#### MEDIA_ROOT

:   The file path for the media folder

#### DEFAULT_AUTO_FIELD

:   Default primary key field type to use for models that don’t have a field with primary_key=True. Set to `BigAutoField`

#### CORS_ORIGIN_WHITELIST

:   Which domains the server can be hosted

#### API_KEY_CUSTOM_HEADER

:   REST API key header

#### CHANNEL_LAYERS

:   TODO: I don't know what this is please explain
