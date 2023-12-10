# forms.py

## Overview

The forms for the app

## Module Objects

### TagFilterForm

:   Form for a tag filter

:   Fields:

| name | type | details |
| ---- | ---- | ------- |
| `tags` | Multiple choice | Query set is all tags|

### EditProfileForm

:   Form for editing profile

:   Model - [User](./models.md#user)

:   Fields (type from model):

    * `first_name`
    * `last_name`
    * `username`
    * `email`
    * `bio`
    * `profile_image`

### AddWaitlistForm

:   Add email to waitlist

:   Model - [Waitlist](./models.md#waitlist)

:   Fields (type from model):

    * `email`

### AddForumForm

:   Add forum post

:   Model - [Forum](./models.md#forum)

:   Fields (type from model):

    * `topic`
    * `description`

### CustomUserCreationForm

:   Registration

:   Model - [User](./models.md#user)

:   Parent - UserCreationForm. Override: Email is required

:   Fields are given html attributes for client-side verification with `.widget.attrs['attr'] = val`

### CustomAuthForm

:   Login

:   Model - [User](./models.md#user)

:   Parent - UserCreationForm. Override: remove password1 password2
