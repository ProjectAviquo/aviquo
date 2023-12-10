# admin.py

## Overview

View configuration for models in admin view

## Module Objects

### UserAdmin

:   Admin view for users

:   Columns:

    * ID
    * Username

### OpportunityAdmin

:   Admin view for opportunities

:   Columns:

    * name
    * URL
    * [`all_tags`](#all_tags)

:   Search by:

    * name
    * URL
    * description

:   Filter:

    * tags

#### all_tags()

:   Returns tags of the opportunity `obj`

### ForumAdmin

:   Admin view for forum posts

:   Columns:

    * Topic
    * User

### TagAgmin

:   Admin view for tags

:   Columns:

    * Name
    * [`tag_count`](#tag_count)

#### tag_count()

:   How many opportunities with the tag `obj`

### WaitlistAdmin

:   Admin view for waitlisted emails

:   Columns:

    * Email
    * Date

:   Search by email

:   Filter/sort by date
