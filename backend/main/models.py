from django.db import models
from core import settings
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class Tag(models.Model):
    """Global list of tags/keywords applicable to opportunities."""
    name = models.CharField(
        unique=True, max_length=50, verbose_name="Tag", help_text="Example: scholarship, extracurricular activity, etc."
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def clean(self):
        if not self.name.strip():
            raise ValidationError("Tag cannot be empty")


class Opportunity(models.Model):
    """Opportunity that users can browse and filter by tags."""
    name = models.CharField(max_length=200, verbose_name="Opportunity", help_text="Opportunity name/title")
    description = models.TextField(
        max_length=4000, verbose_name="Description", help_text="Detailed description of the opportunity"
    )
    profile_image = models.ImageField(null=True, blank=True, upload_to="opp_images/")
    URL = models.URLField(max_length=200, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name  # Change to return the name for a more descriptive representation

    class Meta:
        ordering = ['name']
        verbose_name_plural = "Opportunities"

    def list_tags(self):
        tags = self.tags.order_by('name')
        return ", ".join([tag.name for tag in tags]) if tags else ""

    bookmarks = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='bookmarked_opportunities')
    bookmarked_users = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='bookmarked_opportunities_set')


class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Categories"


class Waitlist(models.Model):
    email = models.EmailField(max_length=320, blank=False, unique=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        ordering = ["-date_created"]

class User(AbstractUser):
    # other usable fields from AbstractUser:
    #  username, first_name, last_name, email, is_staff, is_active, date_joined, last_login
    profile_image = models.ImageField(null=True, blank=True, upload_to="user_images/")
    bio = models.TextField(verbose_name="Bio", max_length=4000, blank=True, null=True)
    date_registered = models.DateTimeField(auto_now_add=True, null=True)

    following =  models.ManyToManyField('self', blank=True, symmetrical=False, related_name="following_set")
    followers =  models.ManyToManyField('self', blank=True, symmetrical=False, related_name="followers_set")

    followed_opps = models.ManyToManyField(Opportunity, blank=True)
    def __str__(self):
        return str(self.id)

    def get_full_name(self) -> str:
        return super().get_full_name()
