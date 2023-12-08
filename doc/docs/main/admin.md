# admin.py

## Overview

View configuration for models in admin view

## Module objects

### Classes

#### UserAdmin

:   Admin view for users

:   Columns:

    * ID
    * Username

#### OpportunityAdmin

:   Admin view for opportunities

:   Columns:

    * name
    * URL
    * [all_tags](#all_tags)

:   Search by:

    * name
    * URL
    * description

:   Filter:

    * tags

#### OpportunityAdmin.all_tags(self, obj)

:   Returns tags of the opportunity obj
