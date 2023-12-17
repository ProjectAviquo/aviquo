"""
Models for the Base app
"""

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    ### Main user for the app

    ### Fields for the user:

    #### From AbstractUser that are used:

    * Username
    * First name
    * Last name
    * Email
    * Date joined

    #### Added:

    * Bio
    """

    def __init__(self, *args, **kwargs) -> None:
        bio: models.Field = models.TextField(
            max_length=796
        )  # Dont ask why 796, trust me bro

        super(AbstractUser, self).__init__(*args, **kwargs)
